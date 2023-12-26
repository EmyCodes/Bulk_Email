#!/usr/bin/python3
import os


participants = [
    {"name": "Ogundare Olamide Emmanuel", "email": "ogundareolamideemmanuel@gmail.com"},
    {"name": "Ogundare Olamide Emmanuel", "email": "ogundareoemts@gmail.com"}
]


subject = "Reminder: Check-In Today at 6:00PM for FIT CAMP 2023"


file_path = os.path.join(os.path.dirname(__file__), "body.html")

with open(file_path, mode="r", encoding="utf-8") as f:
    body = f.read()
