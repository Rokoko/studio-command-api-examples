
# StartRecordingExample.py
# Collection of Command API examples
# Rokoko (c) 2022-2023

import requests

IP_ADDRESS = '127.0.0.1' # Replace with actual ip address
PORT = '14053' # Replace with actual port
API_KEY = '1234' # Replace with actual api key
CLIP_NAME = 'MyNewClip' # Clip Name, Optional
TIME_CODE = '00:01:05:00'
FRAME_RATE = '30'
BACK_TO_LIVE = False # should we enter isolation mode after recording or continue in live mode
COMMAND_NAME = 'recording/start'

responce = None
try:
  responce = requests.post(f"http://{IP_ADDRESS}:{PORT}/v1/{API_KEY}/{COMMAND_NAME}",
    json = {
      'filename': CLIP_NAME,
      'time' : TIME_CODE,
      'frame_rate' : FRAME_RATE,
      'back_to_live' : BACK_TO_LIVE
    }
  )
except Exception as e:
  print (e)

if responce is not None:
  print(responce.json())