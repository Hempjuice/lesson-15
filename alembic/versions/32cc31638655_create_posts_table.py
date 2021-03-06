"""Create posts table

Revision ID: 32cc31638655
Revises: 64a6925a9c25
Create Date: 2021-02-19 17:27:13.260331

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32cc31638655'
down_revision = '64a6925a9c25'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('body', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    # ### end Alembic commands ###
