from sqlalchemy import Column, Integer, Numeric, ForeignKey
from sqlalchemy.orm import relationship, backref
from base import Base

class LineItem(Base):
  __tablename__ = 'line_items'
  line_item_id = Column(Integer(), primary_key=True)
  order_id = Column(Integer(), ForeignKey('orders.order_id'))
  cookie_id = Column(Integer(), ForeignKey('cookies.cookie_id'))
  quantity = Column(Integer())
  extended_cost = Column(Numeric(12, 2))
  order = relationship("Order", backref=backref('line_items', order_by=line_item_id))
  cookie = relationship("Cookie", uselist=False)
