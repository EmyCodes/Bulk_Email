#!/usr/bin/python3
from models import send_email
from resources import participants, subject, body


smtp_server = "smtp.gmail.com" # This is for Gmail, It can be changed to any other SMTP server

sender_email = "sender@gmail.com"
sender_password = "sender_password"

for participant in participants:
    personalized_body = body.replace("[Participant's Name]", participant["name"].split()[1])

    send_email(participant["email"], subject, personalized_body)

print("Email sent successfully.")