
# CalibrateExample.py
# Collection of Command API examples
# Rokoko (c) 2022-2023

import requests

IP_ADDRESS = '127.0.0.1' # Replace with actual ip address
PORT = '14053' # Replace with actual port
API_KEY = '1234' # Replace with actual api key
SMARTSUIT_NAME = '' # Optional, empty to use first found paired actor in the scene
COUNTDOWN_DELAY = 0 # Optional
COMMAND_NAME = 'calibrate'

responce = None
try:
  responce = requests.post(f"http://{IP_ADDRESS}:{PORT}/v1/{API_KEY}/{COMMAND_NAME}",
    json = {
      'device_id': SMARTSUIT_NAME,
      'countdown_delay': COUNTDOWN_DELAY,
      'skip_suit' : False,
      'skip_gloves' : False,
      'use_custom_pose' : False,
      'pose' : 'straight-arms-down' # tpose, straight-arms-down, straight-arms-forward
    }
  )
except Exception as e:
  print (e)

if responce is not None:
  print(responce.json())