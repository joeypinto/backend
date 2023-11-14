"""create role table

Revision ID: 2081214b4192
Revises: 668c8cd1e4c9
Create Date: 2022-11-13 21:24:41.284894

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2081214b4192'
down_revision = '668c8cd1e4c9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "role",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("created_on", sa.DateTime(), nullable=True),
        sa.Column("updated_on", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_roles_id"), "role", ["id"], unique=False)
    op.create_index(op.f("ix_roles_name"), "role", ["name"], unique=False)
    op.create_table(
        "user_role",
        sa.Column("user_id", sa.INTEGER(), nullable=False),
        sa.Column("role_id", sa.INTEGER(), nullable=False),
        sa.Column("created_on", sa.DateTime(), nullable=True),
        sa.Column("updated_on", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["role_id"], ["role.id"],),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"],),
        sa.PrimaryKeyConstraint("user_id", "role_id"),
        sa.UniqueConstraint("user_id", "role_id", name="unique_user_role"),
    )


def downgrade() -> None:
    op.drop_table("user_role")
    op.drop_index(op.f("ix_roles_name"), table_name="role")
    op.drop_index(op.f("ix_roles_id"), table_name="role")
    op.drop_table("role")
