from flask import render_template, request, jsonify
from db.db_users import *

def home_function():
    return render_template('index.html')

def home_confirm_function():
    return render_template('index.html')

def register_user_page_function():
    return render_template("register.html")

def register_user_function():
    name = request.form["name"]
    lastName = request.form["lastName"]
    id = request.form["id"]
    age = request.form["age"]
    connectionSQL()
    insert_record(name, lastName, id, age)
    return render_template("confirm.html")

def consult_user_function():
    obj = request.get_json()
    connectionSQL()
    result = consult_user(obj["id"])
    return jsonify(result)