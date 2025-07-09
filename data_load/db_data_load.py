"""Utils for loading data to database."""

import asyncio
from typing import Any
from uuid import UUID

import pandas as pd
from more_itertools import chunked
from sqlalchemy.testing.plugin.plugin_base import logging

from app.constants.model_enums import SystemType
from app.repositories.main_repository import repository
from app.schemas import (
    OldToleranceCreateSchema,
    OldToleranceMappingShema,
    RangeCreateSchema,
    ToleranceCreateSchema,
    ToleranceMatchCreateSchema,
    ToleranceValueCreateSchema,
)
from core.database import db_pool_context

TOLERANCE_PATH = "./../static/tolerances_values.csv"
OLD_TOLERANCE_PATH = "./../static/tol_mapping.csv"


def divide_letters_digits(row: Any) -> tuple[str, int]:
    """Divides complex tolerance name to letters and digits."""
    value = str(row).strip()
    letters = "".join([char for char in value if char.isalpha()])
    digits = int("".join([char for char in value if char.isdigit()]))
    return letters, digits


class DataCsvParserTolerance:
    """Extract data from csv."""

    def __init__(
        self,
        file_path: str,
    ) -> None:
        """Init function."""
        self.file_path = file_path
        self.file = pd.read_csv(file_path)

    def get_all_data(self) -> list[dict]:
        """Cast dataframe to the dict."""
        return self.file.to_dict(orient="records")

    def parse_tolerance(self) -> list[dict]:
        """Parse dataframe for getting unique values of tolerances."""
        unique_tolerances = (
            self.file[["Tolerance"]]
            .dropna()
            .drop_duplicates()
            .reset_index(drop=True)
        )

        tolerance_list = []
        for _, x in unique_tolerances.iterrows():
            letters, digits = divide_letters_digits(x["Tolerance"])

            if not letters or not digits:
                continue

            tolerance = ToleranceCreateSchema(
                iso_letter=letters,
                iso_digit=digits,
                system=SystemType.HOLE
                if letters[0].isupper()
                else SystemType.SHAFT,
            ).model_dump()

            tolerance_list.append(tolerance)

        return tolerance_list

    def parse_ranges(self) -> list[dict]:
        """Parse dataframe for getting unique values of ranges."""
        unique_ranges = (
            self.file[["From", "To"]]
            .dropna()
            .drop_duplicates()
            .reset_index(drop=True)
        )
        return [
            RangeCreateSchema(
                min_value=int(str(x["From"]).strip()),
                max_value=int(str(x["To"]).strip()),
            ).model_dump()
            for _, x in unique_ranges.iterrows()
        ]


class DataCsvParserOldTolerance:
    """Extract data from csv."""

    def __init__(
        self,
        file_path: str,
    ) -> None:
        """Init function."""
        self.file_path = file_path
        self.file = pd.read_csv(file_path, header=None, sep=";", usecols=[0, 1])

    def parse_old_tolerances(self) -> list[dict]:
        """Extract old tolerances names."""
        uq_old_tolerances = (
            self.file[[0]].dropna().drop_duplicates().reset_index(drop=True)
        )
        return [
            OldToleranceCreateSchema(name=str(x[0]).strip()).model_dump()
            for _, x in uq_old_tolerances.iterrows()
        ]

    def parse_old_tolerances_mapping(self) -> list[dict]:
        """Extract tolerances mapping."""
        mapping = self.file[[0, 1]]
        result = []
        for _, x in mapping.iterrows():
            data = OldToleranceMappingShema(
                name=x[0],
                new_name=x[1],
            )
            result.append(data.model_dump())
        return result


class FinderUUID:
    """Class helper for searching ids in data."""

    def __init__(
        self,
        range_data: list[dict],
        tolerance_data: list[dict],
        old_tolerance_data: list[dict],
    ) -> None:
        """Init function."""
        self.range_data = range_data
        self.tolerance_data = tolerance_data
        self.old_tolerance_data = old_tolerance_data

    def get_range_id(
        self,
        min_value: int,
        max_value: int,
    ) -> UUID | None:
        """Searches and returns id for range."""
        for x in self.range_data:
            if min_value == x["min_value"] and max_value == x["max_value"]:
                return x["id"]
        return None

    def get_tolerance_id(
        self,
        iso_letter: str,
        iso_digit: int,
    ) -> UUID | None:
        """Searches and returns id for tolerance."""
        for x in self.tolerance_data:
            if iso_letter == x["iso_letter"] and iso_digit == x["iso_digit"]:
                return x["id"]
        return None

    def get_old_tolerance_id(
        self,
        name: str,
    ) -> UUID | None:
        """Searches and returns id for old tolerance."""
        for x in self.old_tolerance_data:
            if str(name) == str(x["name"]).strip():
                return x["id"]
        return None


async def load_data(
    range_data: list[dict],
    tolerance_data: list[dict],
    old_tolerance_data: list[dict],
    tolerance_value_m2m_data: list[dict],
    tolerance_match_m2m_data: list[dict],
) -> None:
    """Load data in the database."""
    async with db_pool_context() as session:
        await repository.range.create_range_bulk(
            data=range_data,
            session=session,
        )
        await repository.tolerance.create_tolerance_bulk(
            data=tolerance_data,
            session=session,
        )
        await repository.old_tolerance.create_tolerance_bulk(
            data=old_tolerance_data,
            session=session,
        )
        for chunk in chunked(tolerance_value_m2m_data, 300):
            await repository.tolerance_value.create_tolerance_value_bulk(
                data=chunk,
                session=session,
            )
        await repository.tolerance_match.create_tolerance_match_bulk(
            data=tolerance_match_m2m_data,
            session=session,
        )


class PrepareM2MData:
    """Class helper to prepare m2m data."""

    def __init__(
        self,
        finder: FinderUUID,
    ) -> None:
        """Init function."""
        self.finder = finder

    def create_tolerance_value_m2m_data(
        self,
        common_data: list[dict],
    ) -> list[dict]:
        """Creates m2m tolerances values data."""
        result = []
        for x in common_data:
            letters, digits = divide_letters_digits(x["Tolerance"])
            tolerance_id = self.finder.get_tolerance_id(letters, digits)
            range_id = self.finder.get_range_id(x["From"], x["To"])
            row = ToleranceValueCreateSchema(
                tolerance_id=tolerance_id,
                range_id=range_id,
                upper_value=x["Upper"],
                lower_value=x["Lower"],
            )
            result.append(row.model_dump())
        return result

    def create_tolerances_match_m2m_data(
        self,
        common_data: list[dict],
    ) -> list[dict]:
        """Creates m2m tolerances match data."""
        result = []
        for x in common_data:
            letters, digits = divide_letters_digits(x["new_name"])
            tolerance_id = self.finder.get_tolerance_id(letters, digits)
            old_tolerance_id = self.finder.get_old_tolerance_id(x["name"])
            try:
                row = ToleranceMatchCreateSchema(
                    tolerance_id=tolerance_id,
                    old_tolerance_id=old_tolerance_id,
                )
                result.append(row.model_dump())
            except Exception as e:
                logging.error(e)
        return result


if __name__ == "__main__":
    # declare parsers
    tolerance_parser = DataCsvParserTolerance(TOLERANCE_PATH)
    old_tolerance_parser = DataCsvParserOldTolerance(OLD_TOLERANCE_PATH)

    # Parse DB load ready data for single tables
    range_data: list[dict] = tolerance_parser.parse_ranges()
    tolerance_data: list[dict] = tolerance_parser.parse_tolerance()
    old_tolerance_data: list[dict] = old_tolerance_parser.parse_old_tolerances()

    finder = FinderUUID(
        range_data=range_data,
        tolerance_data=tolerance_data,
        old_tolerance_data=old_tolerance_data,
    )
    # prepare data to load to m2m tables
    tolerance_value_data = tolerance_parser.get_all_data()
    tolerance_mapping_data = old_tolerance_parser.parse_old_tolerances_mapping()

    preparation = PrepareM2MData(finder)

    tolerance_value_m2m_data = preparation.create_tolerance_value_m2m_data(
        tolerance_value_data,
    )
    tolerance_match_m2m_data = preparation.create_tolerances_match_m2m_data(
        tolerance_mapping_data,
    )

    # load data
    asyncio.run(
        load_data(
            range_data=range_data,
            tolerance_data=tolerance_data,
            old_tolerance_data=old_tolerance_data,
            tolerance_value_m2m_data=tolerance_value_m2m_data,
            tolerance_match_m2m_data=tolerance_match_m2m_data,
        ),
    )
