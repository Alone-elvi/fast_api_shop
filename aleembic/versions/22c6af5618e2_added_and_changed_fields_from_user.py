"""Added and changed fields from User

Revision ID: 22c6af5618e2
Revises: 72cec3a7d638
Create Date: 2024-06-25 22:16:55.876519

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '22c6af5618e2'
down_revision: Union[str, None] = '72cec3a7d638'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('description', sa.String(), nullable=True))
    op.alter_column('products', 'price',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=True)
    op.add_column('users', sa.Column('phone', sa.String(), nullable=True))
    op.add_column('users', sa.Column('status', sa.String(), nullable=True))
    op.add_column('users', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('favorite_product_id', sa.Integer(), nullable=True))
    op.add_column('users', sa.Column('type', sa.String(), nullable=True))
    op.create_foreign_key(None, 'users', 'products', ['favorite_product_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'type')
    op.drop_column('users', 'favorite_product_id')
    op.drop_column('users', 'created_at')
    op.drop_column('users', 'status')
    op.drop_column('users', 'phone')
    op.alter_column('products', 'price',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=True)
    op.drop_column('categories', 'description')
    # ### end Alembic commands ###