from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///orm.sqlite', echo=True)

Base = declarative_base()

orders = Table('Orders', Base.metadata,
                Column('id', Integer, primary_key=True),
                Column('client_id', Integer, ForeignKey('Clients.id')),
                Column('product_id', Integer, ForeignKey('Products.id')),
                Column('count', Integer),
                Column('all_sum', Integer)
                     )

class Products(Base):
    __tablename__ = 'Products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    count=Column(Integer)

    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count=count

class Clients(Base):
    __tablename__ = 'Clients'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)

    def __init__(self, name, address):
        self.name = name
        self.address = address

# Создание таблицы
Base.metadata.create_all(engine)

# Создание сессии
# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()

# Продукты
session.add_all([Products('Молоко', 50, 100), Products('Хлеб', 15, 200), Products('Майонез', 90, 12)])
# Клиенты
session.add_all([Clients('Боб', 'Москва'), Clients('Джек', 'Астрахань'), Clients('Иван', 'Магадан')])

session.commit()


