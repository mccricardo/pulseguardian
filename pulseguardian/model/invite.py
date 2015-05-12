# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from sqlalchemy import Column, ForeignKey, Integer

from base import Base, db_session


class Invite(Base):
    '''
    Invite class. Will hold invites to Users for PulseUsers.
    '''
    __tablename__ = 'invites'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    pulse_user_id = Column(Integer, ForeignKey('pulse_users.id'),
                           nullable=True)

    @staticmethod
    def new_invite(user_id, pulse_user_id):
        '''
        Creates a new invite for a PulseUser.
        '''
        invite = Invite(user_id=user_id, pulse_user_id=pulse_user_id)

        db_session.add(invite)
        db_session.commit()

        return invite

    def __repr__(self):
        return "<Invite(user='{0}', pulse_user='{1}')>".format(self.user_id,
                                                         self.pulse_user_id)

    __str__ = __repr__
