
# SendStartRecordingMessage.py
#
# Run the script to send start recording message to the Studio
#  modify the arguments on your purpose
#
# Rokoko 2023

import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 14047

args = {'commandName' : "CaptureStart",
        'timecode' : "00:00:00:00",
        'recordingName' : "NewClip",
        'setActiveClip' : 'False',
        }

MESSAGE = "<{commandName}>" \
        "<TimeCode VALUE=\"{timecode}\"/>" \
        "<Name VALUE=\"{recordingName}\"/>" \
        "<SetActiveClip VALUE=\"{setActiveClip}\"/>" \
        "<ProcessID VALUE=\"12345\"/>" \
        "</{commandName}>".format(**args)

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))