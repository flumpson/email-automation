from pybin import mailing

if __name__ == '__main__':
    email_info = mailing.loadData(
        "./csv/creds.csv", "./csv/group1.csv", "Testing 123", "smtp.gmail.com", "./message/intro.txt")
    mailing.sendIntroMessage(email_info[0], email_info[1], email_info[
                     2], email_info[3], email_info[4], email_info[5])
