"""Try fix maps problem Order -> User

Revision ID: d2c33ea1d299
Revises: aabd90b24cb2
Create Date: 2024-06-25 22:50:04.286952

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd2c33ea1d299'
down_revision: Union[str, None] = 'aabd90b24cb2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
