#Thư viện giao tiếp với Arduino
import serial

#Thư viện lấy thời gian và thời gian delay
from time import sleep
import datetime

#Thư viện dùng cho thao tác với database
import pyrebase

#Thư viện dùng cho việc gửi mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Hàm gửi mail
def mail(nhiet_do, thoi_gian ): # biến nhiet_do, thoi_gian lấy từ hàm def main() phía dưới
	if nhiet_do > 40:
		mail_content = f"The time is {thoi_gian}, the temperature is too high: {nhiet_do}"
	if nhiet_do < 10:
		mail_content = f"The time is {thoi_gian}, the temperature is too low: {nhiet_do}"
	#Địa chỉ mail và mật khau
	sender_address = ''
	sender_pass = ''	
	receiver_address = ''

	#Định dạng MIME cho mail
	message = MIMEMultipart()
	message['From'] = sender_address
	message['To'] = receiver_address
	message['Subject'] = 'Warning temperature '   #Tiêu đề mail
	
	#Nội dung và phần đính kèm cho mail
	message.attach(MIMEText(mail_content, 'plain'))
	
	# Thiết lập giao thức SMTP để gửi
	session = smtplib.SMTP('smtp.gmail.com', 587) #sử dụng giao thức SMTP để giao tiếp với máy chủ thư, kết nối không an toàn với cổng 587
	session.starttls() #kích hoạt bảo mật lts
	session.login(sender_address, sender_pass)
	text = message.as_string()
	session.sendmail(sender_address, receiver_address, text)
	session.quit()
	print('Mail Sent successful')

def main():
	config = {
    "apiKey": "AIzaSyB9WqFFMblv8M82Y2LUdM3y8u27_qptkBs",
    "authDomain": "project-77f5f.firebaseapp.com",
    "databaseURL": "https://project-77f5f-default-rtdb.asia-southeast1.firebasedatabase.app",
    "storageBucket": "project-77f5f.appspot.com"
	}
	firebase = pyrebase.initialize_app(config)
	db = firebase.database()
	with serial.Serial("/dev/ttyUSB0", 9600, timeout=0.5) as arduino:
		sleep(0.1)
		if arduino.isOpen():
			print("{} connected!".format(arduino.port))
			while 1:
				now = datetime.datetime.now() # gán hàm lấy thời gian bằng một biến
				x = str(arduino.readline())
				x = x.strip("',b,\,n,r") #lược bỏ ký tự thừa
				if len(x) > 0:
					print(x)
					data = {"Datetime": now.strftime("%Y-%m-%d"), "Time": now.strftime("%H:%M:%S"), "Temp": x}
					db.child("1 Final value").update(data)
					db.child("2 All value").push(data)
					temp = float(x)
					if temp < 10:
						mail(temp,now.strftime("%H:%M:%S"))
						arduino.write(str.encode('1'))

					elif temp > 40:
						mail(temp,now.strftime("%H:%M:%S"))
						arduino.write(str.encode('3'))

					else:
						arduino.write(str.encode('2'))


				
if __name__ == '__main__':
	main()		