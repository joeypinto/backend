"""create user table

Revision ID: 668c8cd1e4c9
Revises: 
Create Date: 2022-11-12 21:10:22.322708

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '668c8cd1e4c9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("username", sa.String(length=255), nullable=True),
        sa.Column("first_name", sa.String(length=255), nullable=True),
        sa.Column("last_name", sa.String(length=255), nullable=True),
        sa.Column("email", sa.String(length=100), nullable=False),
        sa.Column("password", sa.String(length=255), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=True),
        sa.Column("created_on", sa.DateTime(), nullable=True),
        sa.Column("updated_on", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_users_email"), "user", ["email"], unique=True)
    op.create_index(
        op.f("ix_users_username"), "user", ["username"], unique=False
    )
    op.create_index(op.f("ix_users_id"), "user", ["id"], unique=False)


def downgrade() -> None:
    op.drop_table("user")
    op.drop_index(op.f("ix_roles_name"), table_name="role")
    op.drop_index(op.f("ix_roles_id"), table_name="role")
