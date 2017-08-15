
import data as d
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


#modular data loading from dir files
def loadData(credCSV, groupCSV, subjectCSV):
	credDataObj = d.Data(credCSV)
	credDataRow = credDataObj.get_row(0)
	username = credDataRow[0]
	password = credDataRow[1]
	subjectDataObj = d.data(subjectCSV)
	subjectDataRow = subjectDataObj.get_row(0)
	subject = subjectDataRow[0]
	groupDataObj = d.data(groupCSV)
	return (username, password, subject, groupDataObj)



def customMessage(name,school,messageFileName):
	fp = open(messageFileName,'rU')
	message = fp.read()
	message = message.replace("NAME",name)
	message = message.replace("COLLEGE",school)
	return message

def sendIntroMessage(groupData):
	# create data object with data in format: First Last,Email,School(without College)
	dataObj = d.Data(groupData)

	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username,password)
	for x in range(dataObj.get_num_rows()):
		# grab a row
		data = dataObj.get_row(x)

		# only take first name, lose the last
		temp = data[0].split(" ")
		data[0] = temp[0]

		# set the addresses and headers
		fromaddr = 'rdbrandt@colby.edu'
		toaddrs  = data[1]
		msg = MIMEMultipart()
		msg['From'] = fromaddr
		msg['To'] = toaddrs
		msg['Subject'] = data[2]+" Athletics Training"
		body = customMessage(data[0],data[2],"intro.txt")
		msg.attach(MIMEText(body, 'plain'))
		print msg.as_string()
		# print x
		server.sendmail(fromaddr, toaddrs, msg.as_string())
	server.quit()

if __name__ == '__main__':
	sendIntroMessage("group1.csv")


