
# example of reading from a custom stream target (without lz4 compression)
# ROKOKO 2023

import sys
import socket
import time
import json
import csv

HOST, PORT = '', 14043
SAVE_TO_FILE = True

def WriteUnpackedToFile(data):
    if SAVE_TO_FILE:
        
        scene_info = data.get('scene')
        #print (scene_info)
        
        # extract list of assets from packet actors and characters arrays
        assets = ['actors'] + [actor.get('name') for actor in scene_info.get('actors')]
        assets += ['characters'] + [character.get('name') for character in scene_info.get('characters')]

        actors = scene_info.get('actors')
        if len(actors) > 0:
            theActor = actors[0]
            hipPosition = theActor['body']['hip']['position']
            x, y, z = hipPosition['x'], hipPosition['y'], hipPosition['z']
            
        with open(f'frame_{packet_counter}.csv', 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(assets)

def Unpack(data):
    # we make a python dictionary from a received json text data
    info = json.loads(data)
    # optionally, save extracted info into a file
    if SAVE_TO_FILE: WriteUnpackedToFile(info)

#
## Main loop

start_time = time.time()
fps_counter = 0
packet_counter = 0

# start non blocking UDP listening from a PORT

print ("Start listener at port {}".format(PORT))
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))
s.setblocking(0)

while True:
    try:
        data, address = s.recvfrom(20000)
        Unpack(data)

    except socket.error:
        pass
    else:
        packet_time = time.time()
        fps_counter += 1
        packet_counter += 1

        if (packet_time - start_time) > 1.0:
            
            print (f"received {fps_counter} packets in a second", end='\r')
            
            start_time += 1.0
            fps_counter = 0