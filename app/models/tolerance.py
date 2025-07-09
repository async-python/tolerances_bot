"""Tolerance database table."""

from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates

from app.constants.model_enums import SystemType
from core.database import Base, TimestampMixin, UUIDMixin

if TYPE_CHECKING:
    from app.models import OldTolerance, Range


class Tolerance(Base, UUIDMixin, TimestampMixin):
    """Tolerances database table model."""

    __tablename__ = "tolerances"
    __table_args__ = (
        UniqueConstraint(
            "iso_letter",
            "iso_digit",
            name="uq_tolerance_letter_digit",
        ),
        CheckConstraint("iso_digit >= 0"),
    )

    iso_letter: Mapped[str] = mapped_column(
        String(5),
        nullable=False,
        comment="ISO only letter for tolerance",
    )
    iso_digit: Mapped[int] = mapped_column(
        nullable=False,
        comment="ISO only digit for tolerance",
    )

    system: Mapped[SystemType] = mapped_column(
        nullable=False,
        comment="Calculated system: HOLE or SHAFT",
    )

    # relations
    linked_old_tolerances: Mapped[list["OldTolerance"] | None] = relationship(
        back_populates="linked_tolerances",
        secondary="tolerance_matches",
        lazy="selectin",
    )

    linked_ranges: Mapped[list["Range"] | None] = relationship(
        back_populates="linked_tolerances",
        secondary="tolerance_values",
        lazy="selectin",
    )

    @validates("iso_letter")
    def _auto_set_system(self, key: str, iso_letter_value: str) -> str:
        # Define HOLE/SHAFT
        self.system = (
            SystemType.HOLE
            if iso_letter_value and iso_letter_value[0].isupper()
            else SystemType.SHAFT
        )
        return iso_letter_value
