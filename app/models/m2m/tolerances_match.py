"""Tolerance matches values database table."""

from uuid import UUID as _PY_UUID

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from core.database import Base, TimestampMixin, UUIDMixin


class ToleranceMatch(Base, UUIDMixin, TimestampMixin):
    """Tolerance matches database table model."""

    __tablename__ = "tolerance_matches"
    __table_args__ = (
        UniqueConstraint(
            "tolerance_id",
            "old_tolerance_id",
            name="uq_tolerance_match",
        ),
    )

    tolerance_id: Mapped[_PY_UUID] = mapped_column(
        ForeignKey(
            "tolerances.id",
            ondelete="CASCADE",
        ),
    )
    old_tolerance_id: Mapped[_PY_UUID] = mapped_column(
        ForeignKey(
            "old_tolerances.id",
            ondelete="CASCADE",
        ),
    )
