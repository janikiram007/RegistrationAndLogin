# templates/register.html

from flask import Flask, request, render_template,session,flash
import os
#import sqlite3 as sql
from listdb import *
app = Flask(__name__)
#Bootstrap(app)

@app.route('/')
def hello_world():
    return render_template('register.html')

@app.route('/registerNav/', methods=['GET','POST'])
def registerLink():
    return render_template('register.html')

@app.route('/register/', methods=['GET', 'POST'])
def register():
    username=request.form["username"]
    password=request.form["password"] 
    firstname=request.form["firstname"]
    lastname=request.form["lastname"]
    email=request.form["email"]
    di = {'username':username, 'password':password,'firstname':firstname, 'lastname':lastname,'email':email}
    addRec(di)
    return render_template('login.html')

@app.route('/loginNav/', methods=['GET','POST'])
def loginNav():
    return render_template('login.html')

@app.route('/countme/<input_str>')
def count_me(input_str):
    return input_str

@app.route('/login/', methods=['GET', 'POST'])
def login():
    username = str(request.form['username'])
    password = str(request.form['password'])
    if validate(username,password):
        di = validate(username,password)
        return "<center><h2> Hi "+username+ "<br> Your Name is "+ di['firstname'] +"  "+ di['lastname'] +"<br> your email id is "+di['email'] + "</h2></center>"
    return render_template('invlogin.html')
if __name__ == '__main__':
 # app.secret_key = os.urandom(12)
    app.run()