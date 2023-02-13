from sqlalchemy import Column, Integer, Numeric, String
from base import Base

class Cookie(Base):
  __tablename__ = 'cookies'
  cookie_id = Column(Integer(), primary_key=True)
  cookie_name = Column(String(50), index=True)
  cookie_recipe_url = Column(String(255))
  cookie_sku = Column(String(55))
  quantity = Column(Integer())
  unit_cost = Column(Numeric(12, 2))

  def __repr__(self):
    return "Cookie(cookie_name='{self.cookie_name}', " \
                  "cookie_recipe_url='{self.cookie_recipe_url}', " \
                  "cookie_sku='{self.cookie_sku}', " \
                  "quantity={self.quantity}, " \
                  "unit_cost={self.unit_cost})".format(self=self)
