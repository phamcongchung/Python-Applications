import os
import re
from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message
from pyrebase import pyrebase
from time import sleep

app = Flask(__name__)


app.config["MAIL_DEFAULT_SENDER"] = ""
app.config["MAIL_PASSWORD"] = ""
app.config["MAIL_PORT"] = 587
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = ""
mail = Mail(app)

firebase_config= {
"apiKey": "AIzaSyCpHdlRv79c-MPD_jqJ_1unD1lsRgiR5mU",
"authDomain": "lm35-firebase.firebaseapp.com",
"databaseURL":"https://lm35-firebase-default-rtdb.firebaseio.com",
"storageBucket": "lm35-firebase.appspot.com"
}

firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
	temperature=""
	day=""
	month=""
	year=""
	clock=""
	objects = db.child("value").child("1-set").get()
	for object in objects.each():
		if (object.key()=="temperature"):
			temperature+=object.val()
		if (object.key()=="day"):
			day+=object.val()
		if (object.key()=="month"):
			month+=object.val()
		if (object.key()=="year"):
			year+=object.val()
		if (object.key()=="time"):
			clock+=object.val()
	time=day+"/"+month+"/"+year+"  "+clock
	
	email= request.form.get("email")
	if not email:
		return render_template("error.html")

	subject="This is the warning about the temperature"
	body_text = f"The time is {time}, temperature is {temperature}" 

		
    # Send email
	message = Message(subject=subject, recipients=[email])
	message.body=body_text
	
	mail.send(message)
	
	return render_template("success.html")


if __name__==  "__main__":
    app.run()
