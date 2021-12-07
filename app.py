import re
from flask import Flask, app, request
from flask.templating import render_template
from models import *
from models import Userlog
import hashlib
g_id = 0
# app = Flask(__name__)

# creating obj of userlog to get the id

get_id = Userlog()
print("hello this is id",get_id.id)

@app.route("/test")
def home():
    return "Hello world"

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/login')
def loginPage():
    return render_template('login.html')


@app.route('/register')
def registerPage():
    return render_template('register.html')
    

@app.route('/registersuccess', methods = ["POST"])
def registersuccess():
    
    if request.method == "POST":
        global g_id
        g_id += 1
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        print(name)
        entry = Userlog( id = g_id ,name = name, email = email,password = password)  
        db.session.add(entry)
        db.session.commit()

        return render_template('login.html')



@app.route('/loginsuccess',methods = ["POST"])
def loginsuccess():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        result = db.session.query(Userlog).filter(Userlog.email == email, Userlog.password == password)
        for row in result:
            if len(row.email)!= 0:          # we got that email and password matching in our db
                print("welcome",row.name)
                return render_template('dashboard.html',data=row.name)
        data = "wrong credentials"
        return render_template('login.html', data=data)


if __name__ == "__main__":
    app.run(debug=True, port=3001)
