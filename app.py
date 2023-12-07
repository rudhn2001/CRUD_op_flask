from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db = SQLAlchemy(app)

# ---------------CLASS ORDER 

class Order(db.Model):

# ---------------MAKING A TABLE AND ITS COLUMNS
    __tablename__ = 'orders'

    order_id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(80), unique=False, nullable=True)
    email = db.Column(db.String(120), unique=False, nullable=True)
    street = db.Column(db.String(120), unique=False, nullable=True)
    city = db.Column(db.String(120), unique=False, nullable=True)
    state = db.Column(db.String(120), unique=False, nullable=True)
    postal_code = db.Column(db.Integer, unique=False, nullable=True)
    product_name = db.Column(db.String(120), unique=False, nullable=True)
    quantity = db.Column(db.Integer, unique=False, nullable=True)
    order_date = db.Column(db.String(120), unique=False, nullable=True)
    priority = db.Column(db.Integer, unique=False, nullable=True)

    def json(self):
        return {'order_id': self.order_id,'customer_name': self.customer_name, 'email': self.email, 'street':self.street, 'city':self.city, 'state':self.state, 'postal_code':self.postal_code, 'product_name':self.product_name, 'quantity':self.quantity, 'order_date':self.order_date, 'priority':self.priority}

db.create_all()

#create a test route
@app.route('/test', methods=['GET'])
def test():
  return make_response(jsonify({'message': 'Hello world'}), 200)


# ----------------------create a ORder
@app.route('/orders', methods=['POST'])
def create_order():
  try:
    data = request.get_json()
    new_order = Order(customer_name=data['customer_name'], email=data['email'], street=data['street'], city=data['city'], state=data['state'], postal_code=data['postal_code'], product_name=data['product_name'], quantity=data['quantity'], order_date=data['order_date'], priority=data['priority'])
    db.session.add(new_order)
    db.session.commit()
    return make_response(jsonify({'message': 'Order Enlisted'}), 201)
  except e:
    return make_response(jsonify({'message': 'Error in creating orders, try again'}), 500)

# ----------------------get all ORders
@app.route('/orders', methods=['GET'])
def get_orders():
  try:
    orders = Order.query.all()
    return make_response(jsonify([order.json() for order in orders]), 200)
  except e:
    return make_response(jsonify({'message': 'Error in Getting orders, try again'}), 500)

# ----------------------get a order by id
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
  try:
    order = Order.query.filter_by(order_id=order_id).first()
    if order:
      return make_response(jsonify({'order': order.json()}), 200)
    return make_response(jsonify({'message': 'Order not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'Error in Getting orders, try again'}), 500)

# -----------------------update a order
@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
  try:
    order = Order.query.filter_by(order_id=order_id).first()
    if order:
      data = request.get_json()
      order.customer_name = data['customer_name']
      order.email = data['email']
      order.street = data['street']
      order.city = data['city']
      order.state = data['state']
      order.postal_code = data['postal_code']
      order.product_name = data['product_name']
      order.quantity = data['quantity']
      order.order_date = data['order_date']
      order.priority = data['priority']
      db.session.commit()
      return make_response(jsonify({'message': 'Order updated'}), 200)
    return make_response(jsonify({'message': 'Order not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'Error in Getting orders, try again'}), 500)

# -------------------------------------delete a order
@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
  try:
    order = Order.query.filter_by(order_id=order_id).first()
    if order:
      db.session.delete(order)
      db.session.commit()
      return make_response(jsonify({'message': 'Order deleted'}), 200)
    return make_response(jsonify({'message': 'Order not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'Error in Getting orders, try again'}), 500)
