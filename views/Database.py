from abc import ABC, abstractmethod
import mysql.connector
from settings import MYSQL_USER, MYSQL_PASSWORD, DATABASE_NAME


# Interface showing database connection
class SQLConnection:

    def get_mysqldb(self):
        pass

    def connect(self):
        pass

    def close(self):
        pass


# Connects to MySQL without Database
class MySQLConnection(SQLConnection):

    def __init__(
        self,
        host: str = "localhost",
        port: int = 3306,
        user: str = MYSQL_USER,
        password: str = MYSQL_PASSWORD,
    ):
        self.host: str = host
        self.port: int = port
        self.user: str = user
        self.password: str = password
        self.mydb = None
        self.mycursor = None

    def get_mysqldb(self):
        if self.mydb:
            return self.mydb
        raise ValueError("self.mydb is undefined!.")
    
    def connect(self) -> None:
        """
        Void Function used to connect to mysql
        """
        try:
            # Check if self.mydb is already connected to a database or not to avoid Issues with resource management and Leaks
            if self.mydb:
                self.close()

            self.mydb = mysql.connector.connect(
                host=self.host,
                password=self.password,
                port=self.port,
                user=self.user,
            )

            self.mycursor = self.mydb.cursor()

        except mysql.connector.Error as e:
            print(f"Error connecting to the mysql: {e}")
    
    def close(self) -> None:
        # Check if the database is connected
        if self.mydb.is_connected():
            # Close Cursor first
            self.mycursor.close()
            # Close the mysql connection
            self.mydb.close()
            # Reset self.mydb to None
            self.mydb = None
            # Reset self.mydb to None
            self.mycursor = None

# Connects to MySQL Database directly
class MySQLDatabaseConnection(SQLConnection):
    def __init__(
        self,
        dbname: str = DATABASE_NAME,
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
        self.mycursor = None


    def connect(self, database_name: str = None) -> None:
        """
        Void Function used to connect to database

        :database_name: Optional Parameter to provide a new database name incase needed (default: None)
        """
        try:

            # If a new database name was entered it will overwrite the self.dbname variable other wise it is an optional parameter
            if database_name:
                self.dbname = database_name

            # Check if self.mydb is already connected to a database or not to avoid Issues with resource management and Leaks
            if self.mydb:
                self.close()

            self.mydb = mysql.connector.connect(
                host=self.host,
                password=self.password,
                port=self.port,
                user=self.user,
                database=self.dbname,
            )

            self.mycursor = self.mydb.cursor()

        except mysql.connector.Error as e:
            print(f"Error connecting to the database: {e}")

        except TypeError as e:
            print(e)

    def get_mysqldb(self):
        if self.mydb:
            return self.mydb
        raise ValueError("self.mydb is undefined!.")

    def close(self) -> None:
        # Check if the database is connected
        if self.mydb.is_connected():
            # Close Cursor first
            self.mycursor.close()
            # Close the mysql connection
            self.mydb.close()
            # Reset self.mydb to None
            self.mydb = None
            # Reset self.mydb to None
            self.mycursor = None


class MySQLManager:
    def __init__(self, mysql_connection: MySQLConnection):
        self.connection = mysql_connection
    
    def create_database(self, database_name: str) -> None:
        """
        Method used to check if the database exists or not, Note function closes the connection after creating the database.
        """
        try:
            # Our query to get the database
            query: str = "SHOW DATABASES LIKE %s"
            # Values
            values: tuple = (database_name,) # self.dbname
            # Get database
            print(type(self.connection))
            self.connection.mycursor.execute(query,values)
            result = self.connection.mycursor.fetchall()
            
            # Check if database exists
            if result:
                print(f"Database {database_name} Already Exists !")
            else:
                # Create the database
                self.connection.mycursor.execute(f"CREATE DATABASE {database_name}")
                print(f"Database '{database_name}' created.")
            
            self.connection.close()

        except mysql.connector.Error as e:
            print(f"Error creating/checking database: {e}")


# TableCreation Class:
class MySQLTablesManager:
    __tables :list = []

    def __init__(self, mysql_database_connection: MySQLDatabaseConnection):
        self.connection: MySQLDatabaseConnection = mysql_database_connection

    def add(self,table) -> None:
        """
        Appends table to the self.__tables
        """
        self.__tables.append(table)

    def check_table_exists(self, table_name: str) -> bool:
        self.connection.mycursor.execute(f"SHOW TABLES LIKE '{table_name}'")
        result = self.connection.mycursor.fetchone()
        if result:
            print(f"Table '{table_name}' exists.")
            return True
        else:
            print(f"Table '{table_name}' does not exist.")
            return False

    def create_table(self, table_name: str, columns: list[str]) -> None:
        # Make sure database is connected
        if not (self.connection.mydb):
            self.connection.connect()

        if not self.check_table_exists(table_name):
            create_table_query = f"CREATE TABLE {table_name} ({', '.join(columns)})"
            self.connection.mycursor.execute(create_table_query)
            self.connection.mydb.commit()
            print(f"Table '{table_name}' created.")
        else:
            # Code that should be applied here is to see the difference between new table design and old one
                # if it is renaming a column
                    # add to table query variable string
                # if it is deleteing a column
                    # add to table query variabl string
                # if it is adding a new column
                    # add to table query variable string
                
                # execute and commit the query.
            pass
            
        # Close database here
        self.connection.close()
