"""added content column to posts table

Revision ID: e7dbc88bdc7a
Revises: 6008efe8060c
Create Date: 2026-03-04 09:27:03.880479

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e7dbc88bdc7a"
down_revision: Union[str, Sequence[str], None] = "6008efe8060c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column("content", sa.String, nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", "content")
    pass
