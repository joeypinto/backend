"""create role permission module table

Revision ID: 7940f576d01c
Revises: 3e1bb9416442
Create Date: 2023-05-30 17:24:41.952325

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7940f576d01c'
down_revision = 'a543de78acda'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "role_permission",
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column("permission_id",sa.INTEGER(),
                  nullable=False),
        sa.Column("role_id", sa.INTEGER(), nullable=False),
        sa.Column("module_id", sa.INTEGER(), nullable=False),
        sa.ForeignKeyConstraint(["role_id"], ["role.id"],),
        sa.ForeignKeyConstraint(["permission_id"], ["permission.id"],),
        sa.UniqueConstraint("role_id", "permission_id",
                            name="unique_role_permission"),
        sa.PrimaryKeyConstraint("id"),
    )
def downgrade() -> None:
    op.drop_table("role_permission")