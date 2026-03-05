"""added owner_id foreign key in posts table

Revision ID: 4cda373d30cb
Revises: 280a54f27098
Create Date: 2026-03-04 10:08:58.013644

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4cda373d30cb"
down_revision: Union[str, Sequence[str], None] = "280a54f27098"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))

    op.create_foreign_key(
        "fk_posts_owner_id_users",
        "posts",
        "users",
        ["owner_id"],
        ["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("fk_posts_owner_id_users", "posts", type_="foreignkey")

    # Step 2: Drop the column
    op.drop_column("posts", "owner_id")
    pass
