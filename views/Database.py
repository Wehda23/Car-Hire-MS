import mysql.connector
from settings import MYSQL_USER, MYSQL_PASSWORD, DATBASE_NAME



mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
)

mycursor = mydb.cursor()
