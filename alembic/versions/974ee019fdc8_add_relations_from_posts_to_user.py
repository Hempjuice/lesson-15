"""Add relations from posts to user

Revision ID: 974ee019fdc8
Revises: 32cc31638655
Create Date: 2021-02-19 17:27:48.606088

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '974ee019fdc8'
down_revision = '32cc31638655'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'posts', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.drop_column('posts', 'user_id')
    # ### end Alembic commands ###
