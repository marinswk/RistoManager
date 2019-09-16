"""restaurant table

Revision ID: d7dc02732b9d
Revises: 244c3408a7c4
Create Date: 2019-09-13 08:27:01.786363

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7dc02732b9d'
down_revision = '244c3408a7c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('restaurant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=140), nullable=True),
    sa.Column('address', sa.String(length=140), nullable=True),
    sa.Column('opening_hours', sa.String(length=140), nullable=True),
    sa.Column('style', sa.String(length=140), nullable=True),
    sa.Column('menu', sa.String(length=225), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('restaurant')
    # ### end Alembic commands ###