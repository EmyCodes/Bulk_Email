#!/usr/bin/python3
from resources.sender import send_email
from models import participants, subject, body

print("Sending emails...")

for index, participant in participants.iterrows():
    personalized_body = body.replace("[Participant's Name]", participant["Name"].split()[1])
    send_email(participant["Email"], subject, personalized_body)

# for participant in participants:
#     personalized_body = body.replace("[Participant's Name]", participant["name"].split()[1])
#     send_email(participant["email"], subject, personalized_body)