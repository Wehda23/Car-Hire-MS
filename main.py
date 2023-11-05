from flask import Flask
from views.customer import Customers

app = Flask(__name__)

app.add_url_rule(f"/customers/<int:customer_id>", view_func=Customers.as_view("customer-api"))