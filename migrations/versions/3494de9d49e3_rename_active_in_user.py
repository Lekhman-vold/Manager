"""rename active in User

Revision ID: 3494de9d49e3
Revises: 83f216954783
Create Date: 2021-10-01 11:22:27.063877

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3494de9d49e3'
down_revision = '83f216954783'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_active', sa.Boolean(), nullable=True))
    op.drop_column('user', 'active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('active', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('user', 'is_active')
    # ### end Alembic commands ###
