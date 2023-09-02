import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, Text, REAL, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
engine = create_engine('sqlite:///myDatabase.db')


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, index=True)
    e_mail = Column(sqlalchemy.Text)
    password = Column(sqlalchemy.Text)
    transactions = relationship('Transaction', back_populates='users')

class Transaction(Base):
    __tablename__ = 'transactions'
    transaction_id = Column(Integer, primary_key=True, index=True)
    transaction_sum = Column(REAL)
    transaction_date = Column(Text)
    transaction_category = Column(Text)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    users = relationship('User', back_populates='transactions')

Base.metadata.create_all(bind=engine)

