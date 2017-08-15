
import data as d
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


#modular data loading from dir files
def loadData(credCSV, groupCSV,subject, smtp, messageFileName):
	credgroupDataObj = d.Data(credCSV)
	credDataRow = credgroupDataObj.get_row(0)
	fromEmail = credDataRow[0]
	password = credDataRow[1]
	smtp = emailgroupDataObj[1]
	groupgroupDataObj = d.data(groupCSV)
	return (fromEmail, password, subject, smtp, groupgroupDataOb, messageFileName)


#replaces generic terms in txt to form custom, targeted messages
def customMessage(patternArr,replaceArr,messageFileName):
	fp = open(messageFileName,'rU')
	message = fp.read()
	for x in range(len(patternArr)):
		message = message.replace(patternArr[x],replaceArr[x])
	return message

#sends the messages, crafting each one to target the individual
#NOTE the groupDataObj has 3 columns [PERSON_NAME, EMAIL, COMPANY/INSTITUTION]
def sendIntroMessage(fromEmail, password, subject, smtp, groupDataObj, messageFileName):
	server = smtplib.SMTP(smtp)
	server.starttls()
	server.login(fromEmail,password)
	for x in range(groupDataObj.get_num_rows()):
		# grab a row
		data = groupDataObj.get_row(x)
		# only take first name, lose the last
		temp = data[0].split(" ")
		data[0] = temp[0]
		# set the addresses and headers
		msg = MIMEMultipart()
		msg['From'] = fromEmail
		msg['To'] = data[1]
		msg['Subject'] = data[2]+" "+ subject
		body = customMessage(data[0],data[2], messageFileName)
		msg.attach(MIMEText(body, 'plain'))
		print msg.as_string()
		server.sendmail(fromaddr, toaddrs, msg.as_string())
	server.quit()




