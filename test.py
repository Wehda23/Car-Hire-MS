from views.Database import MySQLConnection, MySQLManager
from settings import DATABASE_NAME

# Initiate MySQLConnection, It connects to MySQL but not the Database!
mysql_connection: MySQLConnection = MySQLConnection()

# Connect to mysql
mysql_connection.connect()

# Initiate MySQLManager
mysql_manager: MySQLManager = MySQLManager(mysql_connection)
# Create database
mysql_manager.create_database(DATABASE_NAME)

print(type(mysql_manager))