from email.mime.image import MIMEImage
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

from editable import sender_name, sender_email, sender_password, smtp_server


# Connect to the SMTP server
try:
    smtp_port = 587 # 465 for SSL connections and 587 for TLS connections
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    print("Logged in to email server successfully")
except Exception as e:
    print(f"Error: {e}")
    print("Failed to login to email server")
    exit(1)
def send_email(recipient_email, subject, body):
    """To be updated"""

    # Create the MIME object
    msg = MIMEMultipart()
    msg["From"] = f"{sender_name} <{sender_email}>"
    msg["To"] = recipient_email
    msg["Subject"] = subject

    # Attach the HTML body of the email
    msg.attach(MIMEText(body, "html"))

    # You can uncomment the following lines if you want to attach images
    # church_logo = os.path.join(os.path.dirname(__file__), "images/church_logo.jpg")
    # fit_camp_23 = os.path.join(os.path.dirname(__file__), "images/fit_camp_23.jpg")
    # msg.attach(MIMEImage(open(church_logo, 'rb').read(), name='church_logo.jpg', _subtype='octet-stream'))
    # msg.attach(MIMEImage(open(fit_camp_23, 'rb').read(), name='fit_camp_23.jpg', _subtype='octet-stream'))

    try:
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print(f"Sending email to {recipient_email}")
        print("Email sent successfully!!!")
    except Exception as e:
        print(f"Error: {e}")
        print(f"Failed to send email to {recipient_email}")
        return False

# Quit the server
# server.quit()
