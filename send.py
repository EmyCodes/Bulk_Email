#!/usr/bin/python3
from models.sender import send_email
from resources import participants, subject, body

print("Sending emails...")

for index, participant in participants.iterrows():
    personalized_body = body.replace("[Participant's Name]", participant["Name"].split()[1])
    send_email(participant["Email"], subject, personalized_body)