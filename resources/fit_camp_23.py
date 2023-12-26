#!/usr/bin/python3
import json
import os

participants = [
    {"name": "Olamide Ogundare", "email": "ogundareolamideemmanuel@gmail.com"},
    {"name": "Olamide Ogundare", "email": "ogundareoemts@gmail.com"}
]


subject = "Reminder: Check-In Today at 6:00PM for FIT CAMP 2023"


file_path = os.path.join(os.path.dirname(__file__), "fit_camp_23.html")

with open(file_path, mode="r", encoding="utf-8") as f:
    body = json.load(f)
