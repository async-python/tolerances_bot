"""Enums for postgres database tables."""

from enum import Enum


class SystemType(Enum):
    """Enum for table CompanyInformation."""

    HOLE = "HOLE"
    SHAFT = "SHAFT"
    OTHER = "OTHER"
