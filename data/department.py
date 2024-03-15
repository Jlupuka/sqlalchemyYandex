from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from data.db_session import SqlAlchemyBase


class Department(SqlAlchemyBase):
    __tablename__ = 'departments'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    chief: Mapped[int] = mapped_column(ForeignKey('users.id'))
    email: Mapped[str]
    members: Mapped['User'] = relationship('User', back_populates='departments')
