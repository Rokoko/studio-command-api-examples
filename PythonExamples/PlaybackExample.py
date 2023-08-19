
# PlaybackExample.py
# Collection of Command API examples
# Rokoko (c) 2022-2023

import requests
from flags import Flags

class CommandAPIPlaybackChange(Flags):
    Unknown = 0
    IsPlaying = 1
    CurrentTime = 2
    GoToFirstFrame = 4
    GoToLastFrame = 8
    PlaybackSpeed = 16

IP_ADDRESS = '127.0.0.1' # Replace with actual ip address
PORT = '14053' # Replace with actual port
API_KEY = '1234' # Replace with actual api key
COMMAND_NAME = 'playback'

response = None
try:
  response = requests.post(f"http://{IP_ADDRESS}:{PORT}/v2/{API_KEY}/{COMMAND_NAME}",
    json = {
      'is_playing' : True, # playback play/pause state (only if correspondant flag is applied)
      'current_time' : 0.0, # playback time in seconds (only if correspondant flag is applied)
      'playback_speed' : 1.0,
      'change_flag' : CommandAPIPlaybackChange.IsPlaying # set flag to take control over the play/pause state
    }
  )
except Exception as e:
  print (e)

if response is not None:
  print(response.json())