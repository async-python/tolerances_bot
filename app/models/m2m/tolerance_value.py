"""Tolerance values database table."""

from decimal import Decimal
from uuid import UUID as _PY_UUID

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from core.database import Base, TimestampMixin, UUIDMixin


class ToleranceValue(Base, UUIDMixin, TimestampMixin):
    """Tolerance values database table model."""

    __tablename__ = "tolerance_values"
    __table_args__ = (
        UniqueConstraint(
            "tolerance_id",
            "range_id",
            name="uq_tolerance_range",
        ),
    )

    tolerance_id: Mapped[_PY_UUID] = mapped_column(
        ForeignKey(
            "tolerances.id",
            ondelete="CASCADE",
        ),
    )
    range_id: Mapped[_PY_UUID] = mapped_column(
        ForeignKey(
            "ranges.id",
            ondelete="CASCADE",
        ),
    )
    upper_value: Mapped[Decimal]
    lower_value: Mapped[Decimal]
