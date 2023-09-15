import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Checks(SqlAlchemyBase):
    __tablename__ = 'checks'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    user = orm.relationship('User')