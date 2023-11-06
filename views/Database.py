import mysql.connector
from settings import MYSQL_USER, MYSQL_PASSWORD, DATBASE_NAME


mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
)

mycursor = mydb.cursor()


class MySQLDatabase(mysql.connector):
    def __init__(
        self,
        dbname: str = DATBASE_NAME,
        host: str = "localhost",
        port: int = 3306,
        user: str = MYSQL_USER,
        password: str = MYSQL_PASSWORD,
    ):
        pass


# Write a class to check the database
# Creates database in case does not exist Or Raise Error Database with this name does not exist
# Write class that checks if a table exists, If does not exist create table
