import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pyrebase import pyrebase
from time import sleep


while True:
	firebase_config= {
	"apiKey": "AIzaSyCpHdlRv79c-MPD_jqJ_1unD1lsRgiR5mU",
	"authDomain": "lm35-firebase.firebaseapp.com",
	"databaseURL":"https://lm35-firebase-default-rtdb.firebaseio.com",
	"storageBucket": "lm35-firebase.appspot.com"
	}

	firebase = pyrebase.initialize_app(firebase_config)
	db = firebase.database()	

	temperature=""
	day=""
	month=""
	year=""
	clock=""
	objects = db.child("value").child("1-set").get()
	for object in objects.each():
		if (object.key()=="temperature"):
			temperature+=object.val()
			print(object.val())
		if (object.key()=="day"):
			day+=object.val()
		if (object.key()=="month"):
			month+=object.val()
		if (object.key()=="year"):
			year+=object.val()
		if (object.key()=="time"):
			clock+=object.val()
	time=day+"/"+month+"/"+year+"  "+clock
	print(time)
	print(temperature)

	
	mail_content = f"The time is {time}, the temperature is {temperature}"

	#The mail addresses and password
	sender_address = ''
	sender_pass = ''
	receiver_address = ''
	#Setup the MIME
	message = MIMEMultipart()
	message['From'] = sender_address
	message['To'] = receiver_address
	message['Subject'] = 'Warning temperature '   #The subject line
	#The body and the attachments for the mail
	message.attach(MIMEText(mail_content, 'plain'))
	#Create SMTP session for sending the mail
	session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
	session.starttls() #enable security
	session.login(sender_address, sender_pass) #login with mail_id and password
	text = message.as_string()

	temperature_int = float(temperature)
	if temperature_int >17:
		session.sendmail(sender_address, receiver_address, text)
		session.quit()
		print('Mail Sent successful')
	else:
		print("Mail Sent fail")

	sleep(5)
	