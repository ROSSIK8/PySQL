from sqlalchemy.orm import sessionmaker

from models import *

DSN = 'postgresql://postgres:april082004@localhost:5432/netology_db'

engine = sq.create_engine(DSN)



Session = sessionmaker(bind=engine)
session = Session()

list_of_facts = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Book.publisher).join(Stock).join(Stock.shop).join(Sale).filter(Publisher.last_name == input('Введите фамилию поэта(Пушкин, Грибоедов, Тургенев): ')).all()
max_item_list = max([max(map(lambda x: str(x), elem_), key=len) for elem_ in list_of_facts], key=len)
for item in list_of_facts:
    item_ = list(map(lambda x: str(x), item))
    for elem in item_:
        print(elem.ljust(len(max_item_list) + 5, ' '), end='')
    print()



session.close()