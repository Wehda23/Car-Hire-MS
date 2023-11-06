from flask import Flask
from views.customer_api import Customers
from views.Database import MySQLConnection, MySQLManager
from settings import DATABASE_NAME
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
