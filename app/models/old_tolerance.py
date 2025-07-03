"""Range database table."""

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database import Base, TimestampMixin, UUIDMixin

if TYPE_CHECKING:
    from app.models import Tolerance


class OldTolerance(Base, UUIDMixin, TimestampMixin):
    """Ranges database table model."""

    __tablename__ = "old_tolerances"

    name: Mapped[int] = mapped_column(
        String(10),
        unique=True,
        comment="old system tolerance name",
    )

    # relations
    linked_tolerances: Mapped[list["Tolerance"]] = relationship(
        back_populates="linked_old_tolerances",
        secondary="tolerance_matches",
        lazy="selectin",
    )
