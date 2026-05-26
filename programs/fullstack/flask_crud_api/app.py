from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Placeholder AWS MySQL connection string
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin1234@nhcawsdb.cbs202kom1ca.ap-south-1.rds.amazonaws.com:3306/nhcdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Product model
class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    supplier = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)


# Create Product
@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    product = Product(
        name=data['name'],
        supplier=data['supplier'],
        price=data['price']
    )
    db.session.add(product)
    db.session.commit()
    return jsonify({'id': product.id, 'name': product.name, 'supplier': product.supplier, 'price': product.price}), 201


# Read all Products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([
        {'id': p.id, 'name': p.name, 'supplier': p.supplier, 'price': p.price}
        for p in products
    ])


# Read one Product
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify({'id': product.id, 'name': product.name, 'supplier': product.supplier, 'price': product.price})


# Update Product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    data = request.json
    product.name = data.get('name', product.name)
    product.supplier = data.get('supplier', product.supplier)
    product.price = data.get('price', product.price)
    db.session.commit()
    return jsonify({'id': product.id, 'name': product.name, 'supplier': product.supplier, 'price': product.price})


# Delete Product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted'})

if __name__ == '__main__':
    app.run(debug=True)
