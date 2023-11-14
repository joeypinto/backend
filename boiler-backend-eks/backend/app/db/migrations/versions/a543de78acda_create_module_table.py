"""create module table

Revision ID: a543de78acda
Revises: 6d5ebb85f6c1
Create Date: 2023-05-13 17:15:06.968019

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d5ebb85f6c1'
down_revision = '2081214b4192'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
            'module',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('name', sa.String(), nullable=False, unique=True),
            sa.Column('description', sa.String(), nullable=False, unique=True),            
            sa.Column('created_on', sa.TIMESTAMP(), nullable=False),
            sa.Column('updated_on', sa.TIMESTAMP(), nullable=False),            
            sa.PrimaryKeyConstraint('id')            
        )
    op.create_index(op.f("ix_module_id"), "module",
                    ["id"], unique=False)

def downgrade() -> None:
    op.drop_table('module')
