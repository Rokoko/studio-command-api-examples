
# InfoExample.py
# Collection of Command API examples
# Rokoko (c) 2022

import requests

IP_ADDRESS = '127.0.0.1' # Replace with actual ip address
PORT = '14053' # Replace with actual port
API_KEY = '1234' # Replace with actual api key

response = None
try:
  response = requests.post(f"http://{IP_ADDRESS}:{PORT}/v2/{API_KEY}/info",
    json = {
      'devices_info': True,
      'clips_info': False
    }
  )
except Exception as e:
  print (e)

if response is not None:
  print(response.json())