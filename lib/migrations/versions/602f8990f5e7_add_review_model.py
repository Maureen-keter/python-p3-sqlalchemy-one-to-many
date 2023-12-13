"""Add Review Model

Revision ID: 602f8990f5e7
Revises: d1a73cc6f0d7
Create Date: 2023-12-10 15:37:58.206818

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '602f8990f5e7'
down_revision = 'd1a73cc6f0d7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('game_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], name=op.f('fk_reviews_game_id_games')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    # ### end Alembic commands ###