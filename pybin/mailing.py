
import data as d
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


# modular data loading from dir files
def loadData(credCSV, groupCSV, subject, smtp, messageFileName, patternCSV, replaceCSV):
    credgroupDataObj = d.Data(credCSV)
    credDataRow = credgroupDataObj.get_row(0)
    fromEmail = credDataRow[0]
    password = credDataRow[1]
    smtp = smtp
    groupDataObj = d.Data(groupCSV)
    patternDataObj = d.Data(patternCSV)
    replaceDataObj = d.Data(replaceCSV)
    return (fromEmail, password, subject, smtp, groupDataObj, messageFileName, patternDataObj, replaceDataObj)


# replaces generic terms in txt to form custom, targeted messages
def customMessage(patternArr, replaceArr, message):
    for x in range(len(patternArr)):
        message = message.replace(patternArr[x], replaceArr[x])
    return message

# sends the messages, crafting each one to target the individual
# NOTE the groupDataObj has 3 columns [PERSON_NAME, EMAIL, COMPANY/INSTITUTION]
def sendIntroMessage(fromEmail, password, subject, smtp, groupDataObj, messageFileName, patternDataObj, replaceDataObj):
    server = smtplib.SMTP(smtp)
    server.starttls()
    server.login(fromEmail, password)
    fp = open(messageFileName, 'rU')
    message = fp.read()
    for x in range(groupDataObj.get_num_rows()):
        # grab a row
        groupData = groupDataObj.get_row(x)
        # only take first name, lose the last
        temp = groupData[0].split(" ")
        groupData[0] = temp[0]
        # set the addresses and headers
        msg = MIMEMultipart()
        msg['From'] = fromEmail
        msg['To'] = groupData[1]
        msg['Subject'] = groupData[2] + " " + subject
        body = customMessage(patternDataObj.get_row(
            0), replaceDataObj.get_row(x), message)
        msg.attach(MIMEText(body, 'plain'))
        print msg.as_string()
        server.sendmail(fromEmail, groupData[1], msg.as_string())
    server.quit()
