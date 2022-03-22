"""Small example OSC client

This program sends 10 random values between 0.0 and 1.0 to the /filter address,
waiting for 1 seconds between each value.
"""
import argparse
import random
import time

from pythonosc.udp_client import SimpleUDPClient
import numpy as np 
import time

# Create Open  sound control UDP server
ip = "127.0.0.1"
port = 1337
client = SimpleUDPClient(ip, port)  # Create client

print('Running OSC server')

# frequency of simulated signal
freq = 5
start = time.time()

while True:
    curTime = time.time() - start
    random_value = np.sin(2*np.pi*freq*curTime)
    client.send_message("/data", random_value)   # Send float message
    time.sleep(0.01)
