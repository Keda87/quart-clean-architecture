"""create user table

Revision ID: 8724a035936a
Revises: 
Create Date: 2019-09-21 08:40:29.603177

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8724a035936a"
down_revision = None
branch_labels = None
depends_on = None

TABLE_NAME = "users"


def upgrade():
    op.create_table(
        TABLE_NAME,
        sa.Column("id", sa.BigInteger, primary_key=True),
        sa.Column("name", sa.String(120), nullable=False),
        sa.Column("email", sa.String(120), nullable=False),
    )


def downgrade():
    op.drop_table(TABLE_NAME)
