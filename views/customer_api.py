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
        data: dict = request.get_json()

        # check keys in data
        if "name" in data and 'email' in data:
            name: str = data['name']
            email: str = data['email']

            # Make sure a user with the same email does not exist
            mysql: MySQLDatabaseConnection = MySQLDatabaseConnection()
            # Connect to database
            mysql.connect()

            query: str = "SELECT * FROM customers WHERE customer_id = %s"
            mysql.mycursor.execute(query, (customer_id,))
            result = mysql.mycursor.fetchall()

            if result:
                # Update the user details
                update_query = "UPDATE customers SET name = %s, email = %s WHERE customer_id = %s"
                values = (name, email, customer_id)
                mysql.mycursor.execute(update_query, values)
                mysql.mydb.commit()
                mysql.close()

                return make_response(jsonify("User details updated!"), 200)
            
            return make_response(jsonify("User does not exist!"), 404)

        return make_response(jsonify("Invalid request data"), 400)

    def delete(self, customer_id):
        """
        Delete a customer by customer_id.
        """
        mysql: MySQLDatabaseConnection = MySQLDatabaseConnection()
        # Connect to database
        mysql.connect()

        # Check if the user exists
        query = "SELECT * FROM customers WHERE customer_id = %s"
        mysql.mycursor.execute(query, (customer_id,))
        result = mysql.mycursor.fetchall()

        if result:
            # Delete the user
            delete_query = "DELETE FROM customers WHERE customer_id = %s"
            mysql.mycursor.execute(delete_query, (customer_id,))
            mysql.mydb.commit()
            mysql.close()
            return make_response(jsonify("User deleted!"), 200)  

        return make_response(jsonify("User does not exist!"), 404) 