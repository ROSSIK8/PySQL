from random import randint as r
from sqlalchemy.orm import sessionmaker

from models import *

DSN = 'postgresql://postgres:april082004@localhost:5432/netology_db'

engine = sq.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

publisher_1 = Publisher(last_name='Пушкин')
publisher_2 = Publisher(last_name='Тургенев')
publisher_3 = Publisher(last_name='Грибоедов')

session.add_all([publisher_1, publisher_2, publisher_3])
session.commit()


book_1_1 = Book(title='Евгение Онегин', publisher=publisher_1)
book_1_2 = Book(title='Капитанская дочка', publisher=publisher_1)
book_1_3 = Book(title='Медный всадник', publisher=publisher_1)

book_2_1 = Book(title='Муму', publisher=publisher_2)
book_2_2 = Book(title='Отцы и дети', publisher=publisher_2)
book_2_3 = Book(title='Нахлебник', publisher=publisher_2)

book_3_1 = Book(title='Горе от ума', publisher=publisher_3)
book_3_2 = Book(title='Притворная неверность', publisher=publisher_3)

list_books = [book_1_1, book_1_2, book_1_3,
              book_2_1, book_2_2, book_2_3,
              book_3_1, book_3_2]

session.add_all(list_books)
session.commit()


shop_1 = Shop(name='Магазин №1')
shop_2 = Shop(name='Магазин №2')
shop_3 = Shop(name='Магазин №3')

list_shops = [shop_1, shop_2, shop_3]

session.add_all(list_shops)
session.commit()


for shop in list_shops:
    for book in list_books:
        session.add(Stock(book=book, shop=shop, count=r(10, 100)))
session.commit()


for id in range(len(list_shops) * len(list_books)):
    id += 1
    session.add(Sale(price=r(100, 1000), date_sale=f'{r(1, 28)}-{r(1, 12)}-{r(2021, 2023)}', id_stock=id, count=r(1, 10)))

session.commit()


session.close()
