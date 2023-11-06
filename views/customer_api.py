from flask.views import MethodView
from flask import jsonify


class Customers(MethodView):
    init_every_request = False

    def get(self, customer_id):
        """
        Retrieve customer's details by customer_id.
        """
        return jsonify({"test": "Test"})

    def post(self, customer_id):
        """
        Add a new customer.
        """
        pass

    def put(self, customer_id):
        """
        Update customer's details by customer_id.
        """
        pass

    def delete(self, customer_id):
        """
        Delete a customer by customer_id.
        """
        pass
