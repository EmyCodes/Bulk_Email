#!/usr/bin/python3
import os
from pandas import read_excel

# participants = [
#     {"name": "Ogundare Olamide Emmanuel", "email": "ogundareolamideemmanuel@gmail.com"},
#     {"name": "Ogundare Olamide Emmanuel", "email": "ogundareoemts@gmail.com"}
#     # Add other mail addresess here
# ]

excel_file_path = os.path.join(os.path.dirname(__file__), "recipients.xlsx")
participants = read_excel(excel_file_path)

subject = "Reminder: Check-In Today at 6:00PM for FIT CAMP 2023"


file_path = os.path.join(os.path.dirname(__file__), "body.html")
with open(file_path, mode="r", encoding="utf-8") as f:
    body = f.read()
