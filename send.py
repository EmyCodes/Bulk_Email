#!/usr/bin/python3
from models.sender import send_email
from resources import participants, subject, body

print("Sending emails...")

for index, participant in participants.iterrows():
    personalized_body = body.replace("[Participant's Name]", participant["Name"].split()[1])

    print(f"Sending email to {participant['Email']}")
    send_email(participant["Email"], subject, personalized_body)
    print(f'Email sent to {participant["Email"]}')

print("All emails sent successfully")