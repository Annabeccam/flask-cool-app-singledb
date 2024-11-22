"""empty message

Revision ID: e1e48535c145
Revises: 
Create Date: 2024-11-22 10:21:53.170007

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1e48535c145'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=False),
    sa.Column('role', sa.String(), nullable=True),
    sa.CheckConstraint("role IN ('student', 'teacher', 'employee')", name='role_types'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('cars',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('model', sa.String(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ondelete='NO ACTION'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cars')
    op.drop_table('users')
    # ### end Alembic commands ###
