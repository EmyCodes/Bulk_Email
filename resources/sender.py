import yagmail
import os

from editable import sender_name, sender_email, sender_password, smtp_server


# Connect to the SMTP server
yag = yagmail.SMTP(sender_email, sender_password)

def send_email(recipient_email, subject, body):
    """To be updated"""

    # You can uncomment the following lines if you want to attach images
    # church_logo = os.path.join(os.path.dirname(__file__), "images/church_logo.jpg")
    # fit_camp_23 = os.path.join(os.path.dirname(__file__), "images/fit_camp_23.jpg")

    try:
        yag.send(
            to=recipient_email,
            subject=subject,
            contents=[body],
            # attachments=[church_logo, fit_camp_23],
        )
        print(f"Sending email to {recipient_email}")
        print("Email sent successfully!!!")
    except Exception as e:
        print(f"Error: {e}")
        print(f"Failed to send email to {recipient_email}")
        return False

# Optionally, you can close the connection after sending all emails
# yag.close()
