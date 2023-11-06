from flask.views import MethodView
from flask import jsonify


class Customers(MethodView):
    init_every_request = False

    def get(self, customer_id):
        """
        API get end point is used to retrieve customer's details
        """
        return jsonify({"test": "Test"})

    def post(self, customer_id):
        """
        API post end point is used to update customer's details
        """
        pass

    def delete(self, customer_id):
        """
        API post end point is used to delete a customer.
        """
        pass
