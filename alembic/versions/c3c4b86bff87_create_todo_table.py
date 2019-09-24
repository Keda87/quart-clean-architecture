"""create todo table

Revision ID: c3c4b86bff87
Revises: 8724a035936a
Create Date: 2019-09-21 08:40:34.953030

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3c4b86bff87'
down_revision = '8724a035936a'
branch_labels = None
depends_on = None

TABLE_NAME = 'todos'

def upgrade():
    op.create_table(
        TABLE_NAME,
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('name', sa.String(225), nullable=False),
        sa.Column('user_id', sa.BigInteger, sa.ForeignKey('users.id'), nullable=False)
    )


def downgrade():
    op.drop_table(TABLE_NAME)
