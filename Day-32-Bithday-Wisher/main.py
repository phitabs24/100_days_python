##################### Extra Hard Starting Project ######################


# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from random import choice
import datetime

MY_EMAIL = "phitabs24@gmail.com"
MY_PASSWORD = "gfxagorzyrqykbok"

# Load the birthdays CSV file
birthdays_df = pd.read_csv('birthdays.csv')

# Get the current date
today = datetime.date.today()

# Filter the birthdays for today's date
today_birthdays = birthdays_df[(birthdays_df['month'] == today.month) & (birthdays_df['day'] == today.day)]


# Function to send a birthday email
def send_birthday_email(name, email):
    # Select a random letter template
    letter_templates = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']  # Add more templates as needed
    template = choice(letter_templates)

    # Read the letter template
    with open(f'letter_templates/{template}', 'r') as f:
        letter = f.read()

    # Replace the [name] placeholder with the birthday person's name
    letter = letter.replace('[NAME]', name)

    # Set up the email message
    msg = MIMEText(letter)
    msg['Subject'] = 'Happy Birthday!'
    msg['From'] = MY_EMAIL  # Replace with your Gmail email
    msg['To'] = email

    # Send the email via Gmail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(MY_EMAIL, MY_PASSWORD)  # Replace with your Gmail password
    server.sendmail(MY_EMAIL, email, msg.as_string())
    server.quit()


# Send birthday emails to today's birthdays
for index, row in today_birthdays.iterrows():
    send_birthday_email(row['name'], row['email'])

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
