from datetime import datetime
from flask import Flask, render_template, request
from . import app
from . import dataAccess as mydb

@app.route("/")
def Home():
    return render_template("Home.html")

@app.route("/Register/",methods=['POST','GET'])
def Register():
    if request.method=='POST':
        try:
            CUST_TYPE= 1 #1 for Customer
            email=request.form['email']
            phone_number=request.form['phone_number']
            name=request.form['name']
            password=request.form['password']
            if mydb.doRegistration(CUST_TYPE,email,phone_number,name,password)==True:
                return render_template("Register.html",msg="Success")
            else:
                return render_template("Register.html",msg="Registration Failed")
        except:
            return render_template("Register.html",msg="Error!")
    else:
        return render_template("Register.html", msg="Welcome")

@app.route("/Login/",methods=['POST','GET'])
def Login():
    if request.method=='POST':
        try:
            email=request.form['email']
            password=request.form['password']
            user_type=-1
            session_id=""
            valid_user=False
            (valid_user,user_type,session_id) = mydb.doLogin(email,password)
            if valid_user == True:
                return render_template("Login.html",msg="Login Success")
            else:    
                return render_template("Login.html",msg="Login Failed")

        except:
            return render_template("Login.html",msg="Error!")
    else:
        return render_template("Login.html", msg="Welcome")

@app.route("/Payment/")
def Payment():
    return render_template("Payment.html")

@app.route("/Rent/")
def Rent():
    return render_template("Rent.html")

@app.route("/Report_Defects/")
def Report_Defects():
    return render_template("Report_Defects.html")

@app.route("/Check_Order/")
def Check_Order():
    return render_template("Check_Order.html")

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
