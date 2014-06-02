import smtplib
from datetime import datetime
from socket import *

def sendEmail(usr,pw,fromaddr,toaddr):
	
	# Initialize SMTP server
	server = smtplib.SMTP("smtp.gmail.com",587)
	server.starttls()
	server.login(usr,pw)
	
	# Send email
	senddate = datetime.strftime(datetime.now(),'%Y-%m-%d')
	subject = "New AFU version"
	m = "Date: %s\r\nFrom: %s\r\nTo: %s\r\nSubject: %s\r\nX-Mailer: My-Mail\r\n\r\n" %(senddate, fromaddr, toaddr, subject)
	msg = " "
	
	server.sendmail(fromaddr, toaddr, m+msg)
	server.quit()
	
if __name__ == '__main__':
	
	usr = 'craig.verz@gmail.com'
	pw = 'Burner898!'
	fromaddr = 'craig.verz@gmail.com'
	toaddr = 'craig.verzosa@gmail.com'
	
	sendEmail(usr,pw,fromaddr,toaddr)
