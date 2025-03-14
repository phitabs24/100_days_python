import requests
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.environ.get("OWM_API_KEY")
print(API_KEY)
parameters = {
    "lat": 0.416198,
    "lon": 9.467268,
    "appid": API_KEY,
    "units": "metric",
    "cnt": 4,
}


url = "https://api.openweathermap.org/data/2.5/forecast"
response = requests.get(url, params=parameters)
response.raise_for_status()
forcast = response.json()
weather_ids = []
for item in forcast["list"]:
    new_id = [int(data["id"]) for data in item["weather"]]
    weather_ids += new_id

for weather_id in weather_ids:
    if weather_id < 700:
        print("Bring an Umbrella")
        break



