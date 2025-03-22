import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

username = os.environ.get("PIXELA_USERNAME")
TOKEN = os.environ.get("PIXELA_TOKEN")
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
graph_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs"
graph_id = "graph1"


parameters = {
    "token": TOKEN,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=PIXELA_ENDPOINT, json=parameters)
print(f"Create account: {response.text}")

# Create graphs
graph_config = {
    "id": graph_id,
    "name": "Coding Practice",
    "unit": "minuit",
    "type": "float",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(f"Create Graph: {response.text}")


# Post value to the graph
date = "20250321"
pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs/{graph_id}/{date}"

today = datetime.now().strftime("%Y%m%d")
pixel_data = {
    # "date": date,
    "quantity": "59.0",

}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(f"Pixel Update Graph: {response.text}")

# Update Pixel on graph

date = "20250321"
pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs/{graph_id}/{date}"

pixel_data_quantity = {
    "quantity": "59.0",
}

response = requests.put(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(f"Pixel Update Graph: {response.text}")