
import data as d
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


# Credentials (if needed)
username = ''
password = ''

def customMessage(name,school,messageFileName):
	fp = open(messageFileName,'w+')
	
	# print lines
	# message.replace("NAME",name)
	# message.replace("COLLEGE_NAME",school)
	# print message

def sendIntoMessage(groupData):

	data = d.data(groupData)
	fromaddr = 'rdbrandt@colby.edu'
	toaddrs  = 'rbrandt810@gmail.com'
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddrs
	msg['Subject'] = "Python email"

	# body = """\n"""



	signoff = "Best,\nRyan Brandt\nColby 2016"
	body+=signoff
	msg.attach(MIMEText(body, 'plain'))

customMessage("tits","titsacademy","intro.txt")



# server = smtplib.SMTP('smtp.gmail.com:587')
# server.starttls()
# server.login(username,password)
# server.sendmail(fromaddr, toaddrs, msg.as_string())
# server.quit()