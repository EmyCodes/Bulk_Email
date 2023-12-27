#!/usr/bin/python3

from email.mime.image import MIMEImage
import smtplib
from sys import argv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

from editable import sender_name,sender_email, sender_password, smtp_server

name = sender_name
email = sender_email
password = sender_password
email_server = smtp_server

def send_email(recipent_email, subject, body):
    """To be updated"""
    sender_email = email
    sender_password = password
    smtp_server = email_server
    smtp_port = 587 #465

    # Create the MIME object
    msg = MIMEMultipart()
    msg["From"] = f"{sender_name} <{sender_email}>"
    msg["To"] = recipent_email
    msg["Subject"] = subject

    # Attach the HTML body of the email

    # church_logo = os.path.join(os.path.dirname(__file__), "images/church_logo.jpg")
    # fit_camp_23 = os.path.join(os.path.dirname(__file__), "images/fit_camp_23.jpg")
    # msg.attach(MIMEImage(open(church_logo, 'rb').read(), name='church_logo.jpg', _subtype='octet-stream'))
    # msg.attach(MIMEImage(open(fit_camp_23, 'rb').read(), name='fit_camp_23.jpg', _subtype='octet-stream'))

    msg.attach(MIMEText(body, "html"))
    # print(type(msg))
    
    # Connect to the SMTP server
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            print("Logged in to email server successfully")
            server.sendmail(sender_email, recipent_email, msg.as_string())
            print(f"Sending email to {recipent_email}")
            print("Email sent successfully!!!")
    except Exception as e:
        print(f"Error: {e}")
        print(f"Failed to send email to {recipent_email}")
        return False
