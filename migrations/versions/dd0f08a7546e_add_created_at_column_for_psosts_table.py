"""add created_at column for psosts table

Revision ID: dd0f08a7546e
Revises: 4f5f2ee2ff80
Create Date: 2021-08-22 12:15:37.707239

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd0f08a7546e'
down_revision = '4f5f2ee2ff80'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'updated_at')
    # ### end Alembic commands ###
