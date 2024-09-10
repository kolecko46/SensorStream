import mysql.connector
import time
from modules import credentials
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = credentials.database_url

engine = create_engine(SQLALCHEMY_DATABASE_URL)

session_local = sessionmaker(autocommit=False,
                             autoflush=False,
                             bind=engine)

Base = declarative_base()



def get_database():
    database = session_local()
    try:
        yield database
    finally:
        database.close()

while True:
    try:
        connection = mysql.connector.connect(
            host = credentials.host,
            user = credentials.user,
            password = credentials.database_psw,
            database = credentials.database
        )
    
        cursor = connection.cursor(buffered=True)
        cursor.execute('SET GLOBAL connect_timeout=6000')
        print("Database connection was succesfull!")
        break
    except Exception as error:
        print("Connection to database failed!")
        print("Error was", error)
        time.sleep(2)


