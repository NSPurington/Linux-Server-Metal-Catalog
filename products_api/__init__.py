from flask import Flask, render_template, request
from flask import redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, products
import random
import string
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)


# Connect to Database and create database session
engine = create_engine('postgresql+psycopg2://products:products@localhost/products')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# JSON APIs to view serializad Product Information
@app.route('/products')
def productsJSON():
    product = session.query(product).all()
    return jsonify(product=[i.serialize for i in product])


@app.route('/product/<int:product_id>')
def alloyJSON(product_id):
    product = session.query(product).filter_by(id=product_id).one()
    alloy = session.query(Alloy).filter_by(product_id=product_id).all()
    return jsonify(Alloy_Item=[i.serialize for i in alloy])


# Show all products
@app.route('/')
@app.route('/products/')
def showproducts():
    products = session.query(product).order_by(asc(product.name))
    if 'username' not in login_session:
        return render_template('publicproducts.html', products=products)
    else:
        return render_template('products.html', products=products)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)
