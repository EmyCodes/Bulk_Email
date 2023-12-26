#!/usr/bin/python3
from models import send_email
from resources import participants, subject, body

for participant in participants:
    personalized_body = body.replace("[Participant's Name]", participant["name"])

    send_email(participant["email"], subject, personalized_body)

print("Email sent successfully.")