from flask import render_template,redirect,url_for,request
from base import app

@app.route('/user', methods=['GET'])
def user():
    try:
        return render_template('user/index.html')
    except Exception as ex:
        print("admin_load_login route exception occured>>>>>>>>>>", ex)


@app.route('/user/shop', methods=['GET'])
def shop():
    try:
        return render_template('user/category-list.html')
    except Exception as ex:
        print("admin_load_login route exception occured>>>>>>>>>>", ex)


@app.route('/user/cart', methods=['GET'])
def cart():
    try:
        return render_template('user/cart.html')
    except Exception as ex:
        print("admin_load_login route exception occured>>>>>>>>>>", ex)


@app.route('/user/checkout', methods=['GET'])
def checkout():
    try:
        return render_template('user/checkout.html')
    except Exception as ex:
        print("admin_load_login route exception occured>>>>>>>>>>", ex)