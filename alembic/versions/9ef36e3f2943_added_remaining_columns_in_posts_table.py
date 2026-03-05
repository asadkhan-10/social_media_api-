"""added remaining columns in posts table

Revision ID: 9ef36e3f2943
Revises: 4cda373d30cb
Create Date: 2026-03-04 10:21:40.565402

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9ef36e3f2943"
down_revision: Union[str, Sequence[str], None] = "4cda373d30cb"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), server_default="TRUE", nullable=False),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
