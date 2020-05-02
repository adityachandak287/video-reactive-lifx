import requests
import os
from dotenv import load_dotenv
load_dotenv()

token = os.getenv("LIFX_ACCESS_TOKEN")

headers = {
    "Authorization": "Bearer %s" % token
}

payload = {
    "power": "on"
}

response = requests.put(
    'https://api.lifx.com/v1/lights/all/state', headers=headers, data=payload)

print(response.json())
