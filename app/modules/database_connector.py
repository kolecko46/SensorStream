import mysql.connector
import time
from modules import credentials

while True:
    try:
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = credentials.database_psw,
            database = "ichannel8_export"
        )
    
        cursor = connection.cursor(buffered=True)
        cursor.execute('SET GLOBAL connect_timeout=6000')
        print("Database connection was succesfull!")
        break
    except Exception as error:
        print("Connection to database failed!")
        print("Error was", error)
        time.sleep(2)