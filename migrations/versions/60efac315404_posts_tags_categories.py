"""posts - tags - categories

Revision ID: 60efac315404
Revises: d0b12fe46119
Create Date: 2018-05-01 15:04:35.507067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60efac315404'
down_revision = 'd0b12fe46119'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=32), nullable=True),
    sa.Column('slug', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tag_slug'), 'tag', ['slug'], unique=True)
    op.create_index(op.f('ix_tag_title'), 'tag', ['title'], unique=True)
    op.create_table('posts_categories',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('post_id', 'tag_id')
    )
    op.create_table('posts_tags',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], ),
    sa.PrimaryKeyConstraint('post_id', 'tag_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts_tags')
    op.drop_table('posts_categories')
    op.drop_index(op.f('ix_tag_title'), table_name='tag')
    op.drop_index(op.f('ix_tag_slug'), table_name='tag')
    op.drop_table('tag')
    # ### end Alembic commands ###
