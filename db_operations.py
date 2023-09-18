from data import db_session
from data.purchases import Purchases


def add_purchase(purchase_name, count, cost):
    db_sess = db_session.create_session()
    purchase = Purchases(
        name=purchase_name,
        count=count,
        cost=cost)
    db_sess.add(purchase)
    db_sess.commit()
    db_sess.close()


def get_purchases():
    db_sess = db_session.create_session()
    ans = db_sess.query(Purchases).all()
    db_sess.close()
    return ans
