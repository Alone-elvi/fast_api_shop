"""Try fix maps problem Order -> User last

Revision ID: 037b4e573770
Revises: 7b35c0a00d15
Create Date: 2024-06-25 22:58:10.666300

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '037b4e573770'
down_revision: Union[str, None] = '7b35c0a00d15'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('user_type', sa.String(), nullable=True))
    op.drop_column('users', 'type')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('type', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('users', 'user_type')
    # ### end Alembic commands ###