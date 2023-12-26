#!/usr/bin/python3
from models.sender import send_email
from resources import participants, subject, body


for participant in participants:
    personalized_body = body.replace("[Participant's Name]", participant["name"].split()[1])

    send_email(participant["email"], subject, personalized_body)

print("Email sent successfully.")