import smtplib
import csv

password = "****"
mailID = "anshuman8800@gmail.com"


message = """
Subject: Regarding auto generated mail
CC: anshuman19@iiitg.ac.in

This message is sent from Python.
Thanks with Regard
Anshuman"""


s = smtplib.SMTP("smtp.gmail.com", 587)
s.ehlo()


s.starttls()
s.login(mailID, password)
with open("contacts_file.csv") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for name, email in reader:
        print(f"Sending email to {name}")
        s.sendmail(mailID, email, message)
s.quit()
