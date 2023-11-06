import mysql.connector
from settings import MYSQL_USER, MYSQL_PASSWORD, DATBASE_NAME


mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
)

mycursor = mydb.cursor()

# Creates database in case does not exist Or Raise Error Database with this name does not exist
class MySQLDatabase(mysql.connector):
    def __init__(
        self,
        dbname: str = DATBASE_NAME,
        host: str = "localhost",
        port: int = 3306,
        user: str = MYSQL_USER,
        password: str = MYSQL_PASSWORD,
    ):
        self.dbname: str = dbname
        self.host: str = host
        self.port: int = port
        self.user: str = user
        self.password: str = password
        self.mydb = None

    def connect(self):
        self.mydb = mysql.connector.connect(
                host = self.host,
                password = self.password,
                port = self.port,
                user = self.user,
                database = self.dbname,
                )
        
    def get_mysqldb(self):
        if self.mydb:
            return self.mydb
        raise ValueError("self.mydb is undefined!.")

    # method to create database

    # method to close connection

# TableCreation Class:
    # Write class that checks if a table exists, If does not exist create table
    # method to check_tables_exists

    # method to create tables
# Write a class to check the database


