from sqlalchemy import create_engine, Column, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

password = input('Password: ')
engine = create_engine('mysql+mysqlconnector://root:%s@localhost:3306/test' % password)
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    book = relationship('Book')


class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    user_id = Column(String(20), ForeignKey('user.id'))


Base.metadata.create_all(engine)

# insert
# user_add = User(id='2', name='Tom')
# session.add(user_add)
# session.commit()
# book = Book(id='1', name='Python从入门到放弃', user_id='2')
# session.add(book)
# session.commit()

# query
user_query = session.query(User).filter(User.id == '2').one()
print(type(user_query), user_query.name)
for book in user_query.book:
    print(book.id, book.name)
for index, book in enumerate(user_query.book):
    print(index, book.id, book.name)

session.close()
