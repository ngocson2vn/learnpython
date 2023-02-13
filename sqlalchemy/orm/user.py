from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from base import Base

class User(Base):
  __tablename__ = 'users'
  user_id = Column(Integer(), primary_key=True)
  username = Column(String(15), nullable=False, unique=True)
  email_address = Column(String(255), nullable=False)
  phone = Column(String(20), nullable=False)
  password = Column(String(25), nullable=False)
  created_on = Column(DateTime(), default=datetime.now)
  updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
