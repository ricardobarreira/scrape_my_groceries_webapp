from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

Base = declarative_base()


class Store(Base):
    __tablename__ = 'stores'

    store_id = Column(Integer(), primary_key=True)
    store_name = Column(String(50))


class Products(Base):
    __tablename__ = 'Products'

    product_id = Column(Integer(), primary_key=True)
    product_name = Column(String(255))
    product_quantity = Column(String(55), nullable=False)


class Offers(Base):
    __tablename__ = 'Offers'

    offer_id = Column(Integer(), primary_key=True)
    offer_price = Column(String(255))
    offer_date = Column(DateTime(), default=datetime.now)
    offer_discount = Column(String(55))

    product_id = Column(Integer(), ForeignKey('Products.product_id'))
    store_id = Column(Integer(), ForeignKey('stores.store_id'))

    product = relationship("Products", uselist=False)
    store = relationship("Store", uselist=False)
