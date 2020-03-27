import os
import random
import smtplib # Email
from dotenv import load_dotenv # For getting stored password
#import getpass # For dynamically enter password

load_dotenv()

username = input("E-mail: ") # e.g. "your_gmail_to_send_from@gmail.com"
password = os.getenv("PASSWORD") # alternatively: getpass.getpass()

def santa_message_body(santa_assigment):
    return f"Your secret santa assignment is {santa_assigment}."

def send_email(to_person, to_email, subject, message_body):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    
    sender_name = "Rami Manna"
    message = f"""From: {sender_name} <{username}>
To: {to_person} <{to_email}>
MIME-Version: 1.0
Content-type: text/html
Subject: {subject}

{message_body}

"""

    server.sendmail(username, to_email, message)
    server.quit()


def send_secret_santas(participants):
    not_gifted = {name for name, email in participants}
    for name, email in participants:
        santa_assigment = random.choice(list(not_gifted - {name}))
        not_gifted.remove(santa_assigment)

        message_body = santa_message_body(santa_assigment)
        subject = "Your Secret Santa Assignment!"
        send_email(name, email, subject, message_body)

PARTICIPANTS = [('Harry Potter', 'potter@hogwarts.edu'), ('Hermione Granger', "hermione@hogwarts.edu")]

if __name__ == "__main__":

    send_secret_santas(PARTICIPANTS)

