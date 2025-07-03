"""Range database table."""

from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, UniqueConstraint
from sqlalchemy.orm import Mapped, relationship

from core.database import Base, TimestampMixin, UUIDMixin

if TYPE_CHECKING:
    from app.models import Tolerance


class Range(Base, UUIDMixin, TimestampMixin):
    """Ranges database table model."""

    __tablename__ = "ranges"
    __table_args__ = (
        CheckConstraint("min_value >= 0", name="check_min_value_positive"),
        CheckConstraint("max_value > 0", name="check_max_value_positive"),
        UniqueConstraint(
            "min_value",
            "max_value",
            name="uq_range_min_value_max",
        ),
    )

    min_value: Mapped[int]
    max_value: Mapped[int]

    linked_tolerances: Mapped[list["Tolerance"] | None] = relationship(
        back_populates="linked_ranges",
        secondary="tolerance_values",
        lazy="selectin",
    )
