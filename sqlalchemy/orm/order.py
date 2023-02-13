from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
from base import Base

class Order(Base):
  __tablename__ = 'orders'
  order_id = Column(Integer(), primary_key=True)
  user_id = Column(Integer(), ForeignKey('users.user_id'))
  shipped = Column(Boolean(), default=False)
  user = relationship("User", backref=backref('orders', order_by=order_id))
