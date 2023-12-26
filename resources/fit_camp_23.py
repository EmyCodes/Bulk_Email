#!/usr/bin/python3
import os

smtp_server = "smtp.gmail.com" # For Gmail, It can be changed to any other SMTP server

sender_email = "sender@gmail.com"
sender_password = "sender_password"

participants = [
    {"name": "Ogundare Olamide Emmanuel", "email": "ogundareolamideemmanuel@gmail.com"},
    {"name": "Ogundare Olamide Emmanuel", "email": "ogundareoemts@gmail.com"}
]


subject = "Reminder: Check-In Today at 6:00PM for FIT CAMP 2023"


file_path = os.path.join(os.path.dirname(__file__), "fit_camp_23.html")

with open(file_path, mode="r", encoding="utf-8") as f:
    body = f.read()
