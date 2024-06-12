from flask import Flask, request,render_template,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import math
import random
from random import randint
from trycourier import Courier
import re
# app=Flask(__name__)
# @app.route("/submit",methods=['POST','GET'])
# def getvalue():
#     if request.method=='POST':
#         x=request.form.get('otp')
#         print(x)
#     return render_template("otpverifactions.html")

# if __name__== "__main__":
#     app.run(debug=True)