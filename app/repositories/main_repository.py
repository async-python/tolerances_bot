"""Collection all repositories."""

from .class_repositories.m2m.tolerance_match_repository import (
    ToleranceMatchRepository,
)
from .class_repositories.m2m.tolerance_value_repository import (
    ToleranceValueRepository,
)
from .class_repositories.old_tolerance_repository import OldToleranceRepository
from .class_repositories.range_repository import RangeRepository
from .class_repositories.tolerance_repository import ToleranceRepository


class MainRepository:
    """Main repository class."""

    def __init__(self: object) -> None:
        """Initialize main repository class."""
        self.range = RangeRepository()
        self.tolerance = ToleranceRepository()
        self.old_tolerance = OldToleranceRepository()
        self.tolerance_value = ToleranceValueRepository()
        self.tolerance_match = ToleranceMatchRepository()


repository = MainRepository()
