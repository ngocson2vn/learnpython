from base import Base
from cookie import Cookie
from user import User
from order import Order
from line_item import LineItem

from sqlalchemy import create_engine
url = "mysql+pymysql://root:12345678@localhost/cookies"
engine = create_engine(url)
Base.metadata.create_all(engine)