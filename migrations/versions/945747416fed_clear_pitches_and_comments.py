"""Clear pitches and comments.

Revision ID: 945747416fed
Revises: 5051beeca5d0
Create Date: 2017-12-22 10:03:35.381525

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '945747416fed'
down_revision = '5051beeca5d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitch_categories', 'image')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitch_categories', sa.Column('image', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
