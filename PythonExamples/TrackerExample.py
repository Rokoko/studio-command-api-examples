
# TrackerExample.py
# Collection of Command API examples
# Rokoko (c) 2022

import requests

IP_ADDRESS = '127.0.0.1' # Replace with actual ip address
PORT = '14053' # Replace with actual port
API_KEY = '1234' # Replace with actual api key
SMARTSUIT_DEVICE_NAME = 'SSE'

responce = None
try:
  responce = requests.post(f"http://{IP_ADDRESS}:{PORT}/v2/{API_KEY}/tracker",
    json = {
      'device_id': SMARTSUIT_DEVICE_NAME,
      'bone_attached': '', # 'Hips'
      'position' : {'X': 1.0, 'Y': 1.0, 'Z': 0.0},
      'rotation' : {'X': 0.0, 'Y': 0.0, 'Z': 0.0, 'W': 1.0},
      'timeout' : 2.0,
      'is_query_only' : True
    }
  )
except Exception as e:
  print (e)

if responce is not None:
  print(responce.json())