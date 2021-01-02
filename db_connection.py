import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db_objects import Store, Products, Offers


# Config setting
def create_session():
    engine = create_engine(os.getenv("DATABASE_URL"))
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def get_products_names():
    session = create_session()
    query = session.query(Products.product_name).order_by(Products.product_name).all()
    session.close()
    return [i[0] for i in query]


def get_full_offers_list(products_list):
    session = create_session()

    query = session.query(Products.product_name, Products.product_quantity, Offers.offer_discount, Offers.offer_price,
                      Store.store_name).join(Store).join(Products).filter(Products.product_name.in_(products_list))

    ordered_by_store_query = query.order_by(Store.store_name)
    ordered_by_name_list = ordered_by_store_query.order_by(Products.product_name).all()
    session.close()
    return ordered_by_name_list




if __name__ == '__main__':
    # get_products_names()
    # get_full_offers_list(['Wiener Würstchen', 'Aus eigener Herstellung Wiener oder Käsewürstchen'])
    pass