from email.mime.text import MIMEText

import requests
from datetime import datetime
import smtplib

# MY_LAT = 3.989718 # Your latitude
# MY_LONG = 9.808647 # Your longitude

MY_LAT = 3.989718 # Your latitude
MY_LONG = 9.808647 # Your longitude

MY_EMAIL = "phitabs24@gmail.com"
MY_PASSWORD = "gfxagorzyrqykbok"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

print(sunrise, sunset)
time_now = datetime.now()
hour = time_now.hour


#If the ISS is close to my current position
# and it is currently dark
if abs(iss_latitude - MY_LAT) < 5 and abs(iss_longitude - MY_LONG) < 5 and hour >= sunset or hour <= sunrise:
    # Then send me an email to tell me to look up.
    msg = MIMEText("The ISS is above you in the sky.")
    msg['Subject'] = "Look Up"
    msg['From'] = MY_EMAIL  # Replace with your Gmail email
    msg['To'] = "subscribeachu@gmail.com"

    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(MY_EMAIL, "subscribeachu@gmail.com", msg.as_string())
    connection.close()



# BONUS: run the code every 60 seconds.



