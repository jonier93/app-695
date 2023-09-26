from server import app
from controller.control import *

@app.route('/')
def home_page():
    return home_function()

@app.route('/home')
def home_confirm_page():
    return home_confirm_function()

@app.route("/register_page")
def register_user_page():
    return register_user_page_function()

@app.route('/register_user', methods=["post"])
def register_user():
    return register_user_function()

@app.route('/consult_user', methods=["post"])
def consult_user():
    return consult_user_function()