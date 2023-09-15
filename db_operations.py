from data import db_session
from data.checks import Checks
from data.purchases import Purchases


def create_check():
    db_sess = db_session.create_session()
    check = Checks()
    db_sess.add(check)
    db_sess.commit()
    db_sess.close()
    return check.id


def add_purchase(check_id, purchase_name, count, cost):
    db_sess = db_session.create_session()
    purchase = Purchases(
        name=purchase_name,
        count=count,
        cost=cost,
        check_id=check_id)
    db_sess.add(purchase)
    db_sess.commit()
    db_sess.close()
    return purchase.id


def get_purchases_from_check(check_id):
    db_sess = db_session.create_session()
    return db_sess.query(Purchases).filter(Purchases.id == check_id).all()