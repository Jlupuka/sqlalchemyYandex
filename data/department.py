from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from data.db_session import SqlAlchemyBase


class Department(SqlAlchemyBase):
    __tablename__ = 'departments'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[Optional[str]]
    chief: Mapped[Optional[int]] = mapped_column(ForeignKey('users.id'))
    members: Mapped[Optional[str]]
    email: Mapped[Optional[str]]

    users = relationship('User', back_populates='department', uselist=True,
                         primaryjoin='Department.id == User.dep_id')
