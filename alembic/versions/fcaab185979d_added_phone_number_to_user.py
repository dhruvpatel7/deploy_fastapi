"""Added Phone number to User

Revision ID: fcaab185979d
Revises: 09931adc0d0d
Create Date: 2023-09-13 12:20:44.622543

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fcaab185979d'
down_revision: Union[str, None] = '09931adc0d0d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###

""" Commands used to automatically generate a revision for changes in 'user' model """
# alembic revision --autogenerate -m "Added Phone number to User" ; to create a revision
# alembic upgrade head ; to push changes