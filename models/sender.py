#!/usr/bin/python3

import smtplib
from sys import argv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from editable import sender_email, sender_password, smtp_server

email = sender_email
password = sender_password
email_server = smtp_server
def send_email(recipent_email, subject, body):
    """To be updated"""
    sender_email = email
    sender_password = password
    smtp_server = email_server
    smtp_port = 587

    # Create the MIME object
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipent_email
    msg["Subject"] = subject

    # Attach the HTML body of the email
    msg.attach(MIMEText(body, "html"))
    
    # Connect to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipent_email, msg.as_string())
