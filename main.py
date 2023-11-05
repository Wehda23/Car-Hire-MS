from flask import Flask
from views.customer_api import Customers
from views.Database import mycursor

app = Flask(__name__)

"""
<============= Database =============>
"""
# In this part of code should run checks for database
# Check if database does not exists
        # Create database with the database name

# Check if table names does not exists
        # Create none existing tables.
        
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
