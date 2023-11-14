"""create permission table

Revision ID: 6d5ebb85f6c1
Revises: 2081214b4192
Create Date: 2022-11-14 01:14:19.301310

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a543de78acda'
down_revision = '6d5ebb85f6c1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "permission",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("module_id", sa.INTEGER(), nullable=False),
        sa.Column("created_on", sa.DateTime(), nullable=True),
        sa.Column("updated_on", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(['module_id'], ['module.id'], onupdate='CASCADE', ondelete='CASCADE'),
    )
    op.create_index(op.f("ix_permissions_id"), "permission",
                    ["id"], unique=False)
    op.create_index(op.f("ix_permissions_name"), 
                    "permission", ["name"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_permissions_name"), table_name="permission")
    op.drop_index(op.f("ix_permissions_id"), table_name="permission")
    op.drop_table("permission")
