"""Actualizacion tabla posteo

Revision ID: 1b71716d29a0
Revises: 
Create Date: 2026-05-23 17:29:59.922161

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1b71716d29a0'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "posteos",
        sa.Column("nombre",sa.String(100),nullable=True)
    )
    pass


def downgrade() -> None:
    op.drop_column("posteos","nombre")
    pass
