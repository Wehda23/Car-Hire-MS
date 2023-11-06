from flask import Flask
from views.customer_api import Customers
from views.Database import MySQLConnection, MySQLManager, MySQLDatabaseConnection,MySQLTablesManager
from settings import DATABASE_NAME
from views.models import CustomersTable, BookingsTable, VehiclesTable

app = Flask(__name__)

"""
<============= Database =============>
"""
# Initiate MySQLConnection, It connects to MySQL but not the Database!
mysql_connection: MySQLConnection = MySQLConnection()

# Connect to mysql
mysql_connection.connect()

# Initiate MySQLManager
mysql_manager: MySQLManager = MySQLManager(mysql_connection)
# Create database
mysql_manager.create_database(DATABASE_NAME)


# Tables
mydb: MySQLDatabaseConnection = MySQLDatabaseConnection()
mydb.connect()
# Initiate MySQLTablesManager instance
table_manager: MySQLTablesManager = MySQLTablesManager(mydb)

# Register tables Note!! it is perferred to be initiated in this order
table_manager.create_table(CustomersTable.name, CustomersTable.fields)
table_manager.create_table(VehiclesTable.name, VehiclesTable.fields)
table_manager.create_table(BookingsTable.name, BookingsTable.fields)


"""
<============= End of Database =============>
"""


"""
<============= API ROUTES =============>
"""
app.add_url_rule(
    f"/customers/<int:customer_id>", view_func=Customers.as_view("customer-api")
)


"""
<============= End of API ROUTES =============>
"""
