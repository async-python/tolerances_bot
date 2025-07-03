"""Database mixins."""

from datetime import datetime
from uuid import UUID as _PY_UUID

from sqlalchemy import TIMESTAMP, UUID, BigInteger
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func


class IntIDMixin:
    """Identifier int mixin."""

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
        index=True,
    )


class UUIDMixin:
    """Identifier uuid mixin."""

    id: Mapped[_PY_UUID] = mapped_column(
        type_=UUID,
        primary_key=True,
        nullable=False,
        index=True,
    )


class TimestampMixin:
    """Timestamp mixin."""

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.current_timestamp(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        onupdate=func.current_timestamp(),
        nullable=True,
    )
