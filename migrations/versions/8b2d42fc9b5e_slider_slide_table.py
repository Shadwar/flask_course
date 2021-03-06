"""slider, slide table

Revision ID: 8b2d42fc9b5e
Revises: b7ca74152ac6
Create Date: 2018-05-02 14:20:30.195873

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b2d42fc9b5e'
down_revision = 'b7ca74152ac6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('slide',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(length=128), nullable=True),
    sa.Column('sort', sa.Integer(), nullable=True),
    sa.Column('slider_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['slider_id'], ['slider.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('slider',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_slider_title'), 'slider', ['title'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_slider_title'), table_name='slider')
    op.drop_table('slider')
    op.drop_table('slide')
    # ### end Alembic commands ###
