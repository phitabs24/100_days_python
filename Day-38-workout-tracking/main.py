"""Work-out tracker using Google Sheets."""


import os
from dotenv import load_dotenv
import requests
from datetime import datetime




load_dotenv()
nutri_id = os.getenv("NUTRITIONIX_APP_ID")
nutri_key = os.getenv("NUTRITIONIX_APP_KEY")

query = input("Tell me what you did: ")

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
gsheet_endpoint = "https://api.sheety.co/de9bbd682e18189dbdd90bcc8965afec/myWorkouts/workouts"

nutri_headers = {
    "x-app-id": nutri_id,
    "x-app-key": nutri_key,
}
sheety_headers = {
    "Authorization": f"Bearer {os.getenv("SHEETY_AUTH")}"
}

parameters = {
    "query": query,
}

nutri_response = requests.post(url=endpoint, json=parameters, headers=nutri_headers)
nutri_response.raise_for_status()
data = nutri_response.json()

now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

for exercise in data["exercises"]:
    exercise_name = exercise["name"].title()
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]

    new_data = {"workout": {
        "date": date,
        "time": time,
        "exercise": exercise_name,
        "duration": duration,
        "calories": calories
    }}
    new_row = requests.post(url=gsheet_endpoint, json=new_data, headers=sheety_headers)
    new_row.raise_for_status()
