import smtplib
from datetime import *
from random import choice

MY_EMAIL = "phitabs24@gmail.com"
MY_PASSWORD = "gfxagorzyrqykbok"

mail_on = True

now = datetime.now()
weekday = now.weekday()

if weekday == 5:
    with open("quotes.txt", "r") as quotes:
        all_quotes = quotes.readlines()
        quote = choice(all_quotes)
    print(quote)
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()

        connection.login(user=MY_EMAIL,
                         password=MY_PASSWORD)

        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs='subscribeachu@gmail.com',
                            msg=f"Subject:Monday Motivation\n\n{quote}")
