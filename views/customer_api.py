from flask.views import MethodView, View
from flask import jsonify, request, make_response
import json
from .Database import MySQLDatabaseConnection


class RegisterCustomers(MethodView):
    init_every_request = False

    def post(self):
        """
        Add a new customer.
        """
        # Grab Data
        data: dict = request.get_json()  # Get data as python dict

        # Make sure a user with the same email does not exist
        mysql: MySQLDatabaseConnection = MySQLDatabaseConnection()
        # Connect to database
        mysql.connect()
        if "name" in data and "email" in data:
            name: str = data["name"]
            email: str = data["email"]

            # Create the Query and execute
            query: str = "SELECT * FROM customers WHERE email = %s"
            mysql.mycursor.execute(query, (email,))

            # Get the result
            result = mysql.mycursor.fetchall()

            # Check if user exists
            if result:
                return make_response(jsonify("User already exists!!"), 409)
            else:
                # Create user
                query: str = "INSERT INTO Customers (name, email) VALUES (%s, %s)"
                values: tuple = (name, email)
                mysql.mycursor.execute(query, values)
                mysql.mydb.commit()

            # Disconnect from database
            mysql.close()
            return make_response(jsonify("User Successfully Created!"))

        return make_response(jsonify("Missing Fields!"), 400)


class Customers(MethodView):
    init_every_request = False

    def get(self, customer_id):
        """
        Retrieve customer's details by customer_id.
        """
        # Make sure a user with the same email does not exist
        mysql: MySQLDatabaseConnection = MySQLDatabaseConnection()
        # Connect to database
        mysql.connect()

        # Create the Query and execute
        query: str = "SELECT * FROM customers WHERE customer_id = %s"
        mysql.mycursor.execute(query, (customer_id,))

        # Get the result
        result = mysql.mycursor.fetchall()

        # Check if user exists
        if result:
            user: dict = {
                "name": result[0][1],
                "email": result[0][2],
            }
            return make_response(jsonify(user))

        mysql.close()
        return make_response(jsonify("User Does not exist!"), 400)

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
