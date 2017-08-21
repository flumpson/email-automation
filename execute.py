from pybin import mailing
import json

if __name__ == '__main__':
    fp = open("settings.json", "rw")
    settings = json.load(fp)
    print settings["credentials_path"]
    email_info = mailing.loadData(settings["credentials_path"], settings["email_metadata_path"],  settings["subject"], settings[
                                  "smtp_server"], settings["message_path"], settings["to_replace_csv_path"], settings["replace_with_csv_path"])
    mailing.sendIntroMessage(email_info[0], email_info[1], email_info[
                             2], email_info[3], email_info[4], email_info[5], email_info[6], email_info[7])
