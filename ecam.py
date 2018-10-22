import os
from time import sleep

def mymail():
		import smtplib 
		from email.mime.multipart import MIMEMultipart 
		from email.mime.text import MIMEText 
		from email.mime.base import MIMEBase 
		from email import encoders 
		   
		fromaddr = "thennavanpmohan@gmail.com"
		toaddr = "siddharthmishra1537@gmail.com"
		   

		msg = MIMEMultipart() 
		 
		msg['From'] = fromaddr 
		  

		msg['To'] = toaddr 
		  

		msg['Subject'] = "We did it finally (-_-)"
		  

		body = "after years and years of hard work 2 boys finally posted their img on gmail"
		  

		msg.attach(MIMEText(body, 'plain')) 
		  
		  
		filename = "ten.jpg"
		attachment = open("/home/dl118/thennavan/program/ten.jpg", "rb") 
		  

		p = MIMEBase('application', 'octet-stream') 
		  

		p.set_payload((attachment).read()) 
		  

		encoders.encode_base64(p) 
		   
		p.add_header('Content-Disposition', "attachment; ten= %s" % filename) 
		  

		msg.attach(p) 
		  

		s = smtplib.SMTP('smtp.gmail.com', 587) 
		  

		s.starttls() 
		  

		s.login(fromaddr, "gmail1943") 
		  

		text = msg.as_string() 
		  

		s.sendmail(fromaddr, toaddr, text) 
		s.quit() 
		return

def takesnap():
	os.system("fswebcam -F 4 /home/dl118/thennavan/program/ten.jpg")
	return

for i in range(10):
	takesnap()
	mymail()
	sleep(5)