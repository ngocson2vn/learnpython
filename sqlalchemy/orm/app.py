from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from cookie import Cookie

url = "mysql+pymysql://root:12345678@localhost/moon"
engine = create_engine(url, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

cookie = Cookie(
  cookie_name='chocolate chip 2',
  cookie_recipe_url='http://some.aweso.me/cookie/recipe.html',
  cookie_sku='CC02',
  quantity=12,
  unit_cost=0.50
)
session.add(cookie)
session.commit()
print(cookie.cookie_id)