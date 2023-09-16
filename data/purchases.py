import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Purchases(SqlAlchemyBase):
    __tablename__ = 'purchases'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    count = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    cost = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    purchase_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)