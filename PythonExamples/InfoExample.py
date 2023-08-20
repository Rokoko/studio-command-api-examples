
# InfoExample.py
# Collection of Command API examples
# Rokoko (c) 2022-2023

import requests

IP_ADDRESS = '127.0.0.1' # Replace with actual ip address
PORT = '14053' # Replace with actual port
API_KEY = '1234' # Replace with actual api key
COMMAND_NAME = 'info'

response = None
try:
  response = requests.post(f"http://{IP_ADDRESS}:{PORT}/v2/{API_KEY}/{COMMAND_NAME}",
    json = {
      'devices_info': True, # return a list of all live devices in the scene
      'clips_info': False, # return a list of all recorded clips in the scene
      'actors_info' : False, # return a list of all actors
      'characters_info' : True # return a list of all character
    }
  )
except Exception as e:
  print (e)
finally:
  if response is not None:
    print(response.json())