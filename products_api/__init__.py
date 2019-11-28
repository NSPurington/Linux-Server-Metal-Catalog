from flask import Flask, render_template, request
from flask import redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc, func
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Product
import random
import string
import httplib2
import json
from flask import make_response
import requests
import simplejson as json

app = Flask(__name__)



# Connect to Database and create database session
engine = create_engine('postgresql+psycopg2://products_user:U$er@localhost/postgres')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# HTTP Landing Page Test
@app.route('/', methods=['GET'])
def pageTest():
    return '''<h1>API Test</h1>
	<p>Landing Page for the API Test app.</p>'''

# JSON APIs to view serialized Products Information for all products
@app.route('/v1/products', methods=['GET'])
def productsJSON():
    items = session.query(Product).all()
    return jsonify(items=[i.serialize for i in items])


# JSON APIs to view serialized Product Information for specific products
@app.route('/v1/product/<int:id>', methods=['GET'])
def productJSON(id):
	#items = session.query(Product).all()
	count = session.query(Product).count()
	if id > count:
		response = make_response(json.dumps("No Product Exists With This ID."), 404)
		response.headers['Content-Type'] = 'application/json'
		return response
	elif id < 1:
		response = make_response(json.dumps("No Product Exists With This ID."), 404)
		response.headers['Content-Type'] = 'application/json'
		return response
	else:
		item = session.query(Product).filter_by(id=id).one_or_none()
		return jsonify(item.serialize)

# Create a new Product
@app.route('/v1/product', methods=['GET', 'POST'])
def newProduct():
    if request.method == 'POST':
        #newProduct = Product(name=requests.json['name'], price=requests.json['price'])
        toAdd = request.get_json(silent=True)
        newProduct = Product(name=toAdd['name'], price=toAdd['price'])
        session.add(newProduct)
        session.commit()
        response = make_response(json.dumps(
            'New Item Added.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
    	error = make_response(json.dumps("Error Adding Product"), 404)
    	response.headers['Content-Type'] = 'application/json'
    	return error


# Delete a Product



if __name__ == '__main__':
    app.debug = True
    #app.run(host='127.0.0.1', port=5432)
    app.run()
