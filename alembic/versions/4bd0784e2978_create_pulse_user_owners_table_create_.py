"""Create pulse_user_owners table. Create keys for other tables.

Revision ID: 4bd0784e2978
Revises: 
Create Date: 2015-05-04 08:44:00.365481

"""

# revision identifiers, used by Alembic.
revision = '4bd0784e2978'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'pulse_user_owners',
        sa.Column('users_id', sa.Integer, sa.ForeignKey('users.id'),
                  nullable=False),
        sa.Column('pulse_users_id', sa.Integer,
                  sa.ForeignKey('pulse_users.id'), nullable=False),
    )

    op.drop_constraint('pulse_users_ibfk_1', 'pulse_users', 'foreignkey')
    op.drop_column('pulse_users', 'owner_id')


def downgrade():
    op.drop_table('pulse_user_owners')
    op.add_column('pulse_users', sa.Column('owner_id', sa.Integer,
                  sa.ForeignKey('users.id')))
