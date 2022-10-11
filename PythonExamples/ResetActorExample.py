
# ResetActorExample.py
# Collection of Command API examples
# Rokoko (c) 2022

import requests

IP_ADDRESS = '127.0.0.1' # Replace with actual ip address
PORT = '14053' # Replace with actual port
API_KEY = '1234' # Replace with actual api key
SMARTSUIT_NAME = 'SSE' # Optional

responce = None
try:
  responce = requests.post(f"http://{IP_ADDRESS}:{PORT}/v2/{API_KEY}/resetactor",
    json = {
      'deviceId': SMARTSUIT_NAME
    }
  )
except Exception as e:
  print (e)

if responce is not None:
  print(responce.json())