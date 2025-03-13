import requests

API_KEY = "d698c2295960276d083047e298eb9ace"
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
        will_rain = True

if will_rain:
    print("Bring an Umbrella")


