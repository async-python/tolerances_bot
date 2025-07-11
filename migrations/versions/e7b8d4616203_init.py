"""init

Revision ID: e7b8d4616203
Revises: 
Create Date: 2025-06-26 17:55:14.890612

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e7b8d4616203'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('old_tolerances',
    sa.Column('name', sa.String(length=10), nullable=False, comment='old system tolerance name'),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_old_tolerances_id'), 'old_tolerances', ['id'], unique=False)
    op.create_table('ranges',
    sa.Column('min_value', sa.Integer(), nullable=False),
    sa.Column('max_value', sa.Integer(), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.CheckConstraint('max_value > 0', name='check_max_value_positive'),
    sa.CheckConstraint('min_value >= 0', name='check_min_value_positive'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('min_value', 'max_value', name='uq_range_min_value_max')
    )
    op.create_index(op.f('ix_ranges_id'), 'ranges', ['id'], unique=False)
    op.create_table('tolerances',
    sa.Column('iso_letter', sa.String(length=5), nullable=False, comment='ISO only letter for tolerance'),
    sa.Column('iso_digit', sa.Integer(), nullable=False, comment='ISO only digit for tolerance'),
    sa.Column('system', sa.Enum('HOLE', 'SHAFT', 'OTHER', name='systemtype'), nullable=False, comment='Calculated system: HOLE or SHAFT'),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.CheckConstraint('iso_digit >= 0'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('iso_letter', 'iso_digit', name='uq_tolerance_letter_digit')
    )
    op.create_index(op.f('ix_tolerances_id'), 'tolerances', ['id'], unique=False)
    op.create_table('tolerance_matches',
    sa.Column('tolerance_id', sa.UUID(), nullable=False),
    sa.Column('old_tolerance_id', sa.UUID(), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['old_tolerance_id'], ['old_tolerances.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['tolerance_id'], ['tolerances.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('tolerance_id', 'old_tolerance_id', name='uq_tolerance_match')
    )
    op.create_index(op.f('ix_tolerance_matches_id'), 'tolerance_matches', ['id'], unique=False)
    op.create_table('tolerance_values',
    sa.Column('tolerance_id', sa.UUID(), nullable=False),
    sa.Column('range_id', sa.UUID(), nullable=False),
    sa.Column('upper_value', sa.Float(), nullable=False),
    sa.Column('lower_value', sa.Float(), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['range_id'], ['ranges.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['tolerance_id'], ['tolerances.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('tolerance_id', 'range_id', name='uq_tolerance_range')
    )
    op.create_index(op.f('ix_tolerance_values_id'), 'tolerance_values', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tolerance_values_id'), table_name='tolerance_values')
    op.drop_table('tolerance_values')
    op.drop_index(op.f('ix_tolerance_matches_id'), table_name='tolerance_matches')
    op.drop_table('tolerance_matches')
    op.drop_index(op.f('ix_tolerances_id'), table_name='tolerances')
    op.drop_table('tolerances')
    op.drop_index(op.f('ix_ranges_id'), table_name='ranges')
    op.drop_table('ranges')
    op.drop_index(op.f('ix_old_tolerances_id'), table_name='old_tolerances')
    op.drop_table('old_tolerances')
    # ### end Alembic commands ###
    op.execute("DROP TYPE systemtype")

