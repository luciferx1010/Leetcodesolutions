import os
from flask import Flask, redirect, render_template, request
from PIL import Image
import torchvision.transforms.functional as TF
import CNN
import numpy as np
import torch
import pandas as pd
import math, random
from email import message
from email.message import EmailMessage
from hashlib import sha1
from flask import Flask, render_template, request,session
from flask_mail import Mail, Message
import math, random
from flask_restful import Resource, Api
import base64
#from merged_code import classify_image
from flask_mysqldb import MySQL
#import uuid
from flask import redirect
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask_session import Session
import traceback
from datetime import datetime
import json
sess = Session()

app = Flask(name)

mail= Mail(app)
# creating an API object

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'atharvpuranik15@gmail.com'
app.config['MAIL_PASSWORD'] = 'wmclnixzllhtenmb'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'leafscan'

port = 587  
smtp_server = "smtp.gmail.com"
sender_email = "atharvpuranik15@gmail.com"  
password = "wmclnixzllhtenmb"

otpmap={}
mysql = MySQL(app)

disease_info = pd.read_csv('disease_info.csv' , encoding='cp1252')
supplement_info = pd.read_csv('supplement_info.csv',encoding='cp1252')

model = CNN.CNN(39)    
model.load_state_dict(torch.load("plant_disease_model_1_latest.pt"))
model.eval()

def prediction(image_path):
    image = Image.open(image_path)
    image = image.resize((224, 224))
    input_data = TF.to_tensor(image)
    input_data = input_data.view((-1, 3, 224, 224))
    output = model(input_data)
    output = output.detach().numpy()
    index = np.argmax(output)
    return index



@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact-us.html')

@app.route('/index')
def ai_engine_page():
    return render_template('index.html')

@app.route('/mobile-device')
def mobile_device_detected_page():
    return render_template('mobile-device.html')

@app.route('/forgot')
def forgot():
    return render_template('forgot.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

def generateOTP() :
    digits = "0123456789"
    OTP = ""
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
 
    return OTP

@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        details = request.form
        session['name'] = details['Name']
        session['email']= details['Email']
        session['password']= details['Password']
        Email=session['email']
        cur = mysql.connection.cursor()
        cur.execute('select * from users where email= %s' , (Email,))
        account=cur.fetchone()
        if account:
            msg1="Email is Already Registered! You Cannot Register With this Email"
            return render_template("indexreg.html",msg1=msg1)

        if details['Name'] == '':
            msg1="Name must be filled"
            return render_template("indexreg.html",msg1=msg1)

        if details['Email'] == '':
            msg1="Email must be filled"
            return render_template("indexreg.html",msg1=msg1)
            
        if details['Password'] == '':
            msg1="Password must be filled"
            return render_template("indexreg.html",msg1=msg1)
        # id = uuid.uuid4()
        # id=str(id)
        # id=id.replace('-','')
        # cur = mysql.connection.cursor()
        # try:
        #     cur.execute("INSERT INTO users (passwordhash, email, name, token) VALUES (sha1(%s), %s, %s, %s)", (Password,Email,Name,id))
        # except:
        #     return 'Fail'
        # mysql.connection.commit()
        # cur.close()
        return redirect("/otpverification?email="+Email)
    return render_template("indexreg.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    msg=''
    msg1=''
    cur = mysql.connection.cursor()
    if request.method == "POST":
        details = request.form
        Email = details['Email']
        Password= details['Password']
        try:
            cur.execute('select * from users where email= %s and passwordhash= sha1(%s)' , (Email,Password,))
            account=cur.fetchone()
            print(account)
            if account:
                session['loggedin'] = True
                session['id'] = account[0]
                session['name'] = account[3]
                session['email'] = account[2]
                msg = 'Logged in successfully !'
                return redirect('/index')
            else:
                print("no account found")
                msg = 'Incorrect username / password !'
                return render_template('indexreg.html', msg = msg)
        except Exception:
            traceback.print_exc()
            return redirect('/')
    cur.close()
    print("rendering indexreg.html")
    return render_template("indexreg.html")

@app.route("/otpverification",methods = ["GET","POST"])
def otpverification():
    genotp=0
    #otpmap={}
    cur = mysql.connection.cursor()
    Email=request.args.get('email') # get from request
    #Email='prathameshpuranik24@gmail.com'
    #print(Email)
    if request.method == "POST":
        details = request.form
        otp = details['otp']
        genotp=otpmap[Email]
        if genotp == otp :
            Name= session['name'] 
            Email= session['email']
            Password=session['password']
            try:
                cur.execute("INSERT INTO users (passwordhash, email, name) VALUES (sha1(%s), %s, %s)", (Password,Email,Name))
            except:
                return redirect('/')
            mysql.connection.commit()
            cur.close()
            del otpmap[Email]
            msg1="Registration is Sucessful"
            return render_template("indexreg.html",msg1=msg1)
        else:
            msg="Registration is Unsucessful!, You Have Entered Incorrect OTP, Create Account Again!"
            return render_template("indexreg.html",msg=msg)
    else:
        genotp=generateOTP()
        otpmap[Email]=genotp
        print(otpmap)
        print(Email)
        SUBJECT = "OTP Verification for LeafScan.Ai Registration"
        TEXT = """\
        Your One Time Password(OTP) for LeafScan.Ai Registration is %s.
        Do Not Share OTP With Anyone.
        """%(str(genotp),)
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, Email, message)

    return render_template("otp.html")



print(mysql)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        image = request.files['image']
        filename = image.filename
        file_path = os.path.join('static/uploads', filename)
        image.save(file_path)
        print(file_path)
        pred = prediction(file_path)
        title = disease_info['disease_name'][pred]
        description =disease_info['description'][pred]
        prevent = disease_info['Possible Steps'][pred]
        image_url = disease_info['image_url'][pred]
        supplement_name = supplement_info['supplement name'][pred]
        supplement_image_url = supplement_info['supplement image'][pred]
        supplement_buy_link = supplement_info['buy link'][pred]
        return render_template('submit.html' , title = title , desc = description , prevent = prevent , 
                               image_url = image_url , pred = pred ,sname = supplement_name , simage = supplement_image_url , buy_link = supplement_buy_link)

@app.route('/market', methods=['GET', 'POST'])
def market():
    return render_template('market.html', supplement_image = list(supplement_info['supplement image']),
                           supplement_name = list(supplement_info['supplement name']), disease = list(disease_info['disease_name']), buy = list(supplement_info['buy link']))

if name == "main":
    print('starting app')
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    sess.init_app(app)
    app.run(host='0.0.0.0')
