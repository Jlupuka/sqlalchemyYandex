import datetime
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from data.db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    surname: Mapped[Optional[str]]
    name: Mapped[Optional[str]]
    age: Mapped[Optional[int]]
    position: Mapped[Optional[str]]
    speciality: Mapped[Optional[str]]
    address: Mapped[Optional[str]]
    email: Mapped[Optional[str]] = mapped_column(unique=True)
    hashed_password: Mapped[Optional[str]]
    modified_date: Mapped[Optional[datetime.datetime]]


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    team_leader: Mapped[int] = mapped_column(ForeignKey(User.id))
    job: Mapped[Optional[str]]
    work_size: Mapped[Optional[int]]
    collaborators: Mapped[Optional[str]]
    start_date: Mapped[Optional[datetime.datetime]]
    end_date: Mapped[Optional[datetime.datetime]]
    is_finished: Mapped[Optional[bool]]
