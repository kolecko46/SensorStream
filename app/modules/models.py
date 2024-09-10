from sqlalchemy import Column, Integer, String, DateTime
from modules.database_connector import Base

class Users(Base):
    __tablename__="users"

    id = Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    first_name = Column(String(100),nullable=False)
    last_name = Column(String(100),nullable=False)
    password = Column(String(100),nullable=False)
    email = Column(String(100),nullable=False,unique=True)

class DHT11_data(Base):
    __tablename__="dht11"

    temperature = Column(String(100),nullable=False)
    humidity = Column(String(100),nullable=False)
    created_at = Column(DateTime,primary_key=True)
