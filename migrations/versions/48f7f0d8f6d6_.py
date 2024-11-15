"""empty message

Revision ID: 48f7f0d8f6d6
Revises: 8210ad46c19f
Create Date: 2024-11-14 20:54:02.094804

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48f7f0d8f6d6'
down_revision = '8210ad46c19f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('loan')
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_available', sa.Boolean(), nullable=True))
        batch_op.drop_column('status')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.VARCHAR(length=20), nullable=True))
        batch_op.drop_column('is_available')

    op.create_table('loan',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('book_id', sa.INTEGER(), nullable=False),
    sa.Column('borrowed_at', sa.DATETIME(), nullable=False),
    sa.Column('returned_at', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
