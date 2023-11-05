from flask.views import MethodView




class Customers(MethodView):
    init_every_request = False

    def get(self, customer_id):
        pass

    def post(self, customer_id):
        pass

    def delete(self, customer_id):
        pass
