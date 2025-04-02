# COPYRIGHT 2025 (C) Ali Al-mayahi
# YOUTUBE: https://youtube.com/@ali_crafty
# TIKTOK: @tr6s_
# INSTAGRAM: @tr6s.i
# FACEBOOK: https://www.facebook.com/profile.php?id=100078004273350
"""
### ASCII Video Streaming Server in Python

This guide explains how to create a **TCP server** in Python that streams an **animated video** using **ASCII art**. The server reads frames from a folder (`frames/`) and sends them over a socket connection to clients, such as `curl`.

---

## (1) How It Works  
1. The server listens for incoming connections.  
2. It loads all ASCII frames from the `frames/` folder.  
3. Once a client connects (e.g., using `curl`), the server continuously sends frames in sequence.  
4. Each frame is preceded by an **ANSI clear screen code (`\033[H\033[J`)** to create an animation effect.  
5. The loop continues until the animation finishes

---
"""


FRAMES_FOLDER_PATH = None # EX: "./frames" (String)
FRAME_TIMEOUT = None # EX: 0.5 # (float/int)
IP_ADDRESS = None # EX: 127.0.0.1 (String)
PORT = None # EX: 777 (int)
FRAMES = None # EX: 10 | How many frames in the folder (int)
COLORFUL = None # EX: True | It's give every frame random color from `COLORS` Keyword (Boolean)

COLORS = [
    # b"\033[30m",  # Black
    b"\033[31m",  # Red
    b"\033[32m",  # Green
    b"\033[33m",  # Yellow
    b"\033[34m",  # Blue
    b"\033[35m",  # Magenta
    b"\033[36m",  # Cyan
    # b"\033[37m",  # White
    b"\033[90m",  # Bright Black (Dark Gray)
    b"\033[91m",  # Bright Red
    b"\033[92m",  # Bright Green
    b"\033[93m",  # Bright Yellow
    b"\033[94m",  # Bright Blue
    b"\033[95m",  # Bright Magenta
    b"\033[96m",  # Bright Cyan
    b"\033[97m",  # Bright White
]

import socket
import time
import threading
import os
import json
import sys
import random

stop_event = threading.Event()

configdefault = {"FRAMES_FOLDER_PATH": "./frames","FRAME_TIMEOUT": 0.5,"IP_ADDRESS": "127.0.0.1","PORT": 777, "COLORFUL": False, "FRAMES": 10}
if os.path.isfile("config.json"):
    config = json.loads(open("config.json", 'r').read())
    if FRAMES_FOLDER_PATH == None:
        try:
            FRAMES_FOLDER_PATH = config['FRAMES_FOLDER_PATH']
        except KeyError:
            FRAMES_FOLDER_PATH = configdefault['FRAMES_FOLDER_PATH']
    
    if FRAME_TIMEOUT == None:
        try:
            FRAME_TIMEOUT = config['FRAME_TIMEOUT']
        except KeyError:
            FRAME_TIMEOUT = configdefault['FRAME_TIMEOUT']
    
    if FRAMES == None:
        try:
            FRAMES = config['FRAMES']
        except KeyError:
            FRAMES = configdefault['FRAMES']
    
    if COLORFUL == None:
        try:
            COLORFUL = config['COLORFUL']
        except KeyError:
            COLORFUL = configdefault['COLORFUL']
    
    if IP_ADDRESS == None:
        try:
            IP_ADDRESS = config['IP_ADDRESS']
        except KeyError:
            IP_ADDRESS = configdefault['IP_ADDRESS']
    
    if PORT == None:
        try:
            PORT = config['PORT']
        except KeyError:
            PORT = configdefault['PORT']


os.makedirs(FRAMES_FOLDER_PATH, exist_ok=True)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((IP_ADDRESS, PORT))
print("[SERVER]", (IP_ADDRESS, PORT))


def control():
    cmd = ''
    try:
        try:
            cmd = input()
        except:
            goodbye()
        if cmd == 'exit': 
            goodbye()
    except KeyboardInterrupt or EOFError:
        goodbye()

threading.Thread(target=control).start()

frames = []

### IMPORT ALL TEXT FILES IN FOLDER AND SAVE IT AS FRAME
# for frame in os.listdir(FRAMES_FOLDER_PATH):
#     if ".txt" in frame:
#         frames.append(open(os.path.join(FRAMES_FOLDER_PATH, frame), 'r').read().encode())

### IMPORT ONLY FRAMES WITH [NUMBER].txt
for i in range(FRAMES):
    fpath = os.listdir(FRAMES_FOLDER_PATH)
    frame_path = os.path.join(FRAMES_FOLDER_PATH, f"{i}.txt")
    if os.path.isfile(frame_path):
        frames.append(open(frame_path, 'r').read().encode())


def proccess_user(conn, addr):
    try:
        header = b"HTTP/1.1 200 OK\r\n\r\n"
        conn.sendall(header)
        with conn.makefile("rwb") as stream:
            while True:
                for frame in frames:
                    if stop_event.is_set():
                        conn.shutdown(socket.SHUT_RDWR)
                        print("[CLOSED]", addr)
                        return
                    stream.write(b'\033[2J\033[3J\033[H')
                    if COLORFUL: stream.write(random.choice(COLORS))
                    stream.write(frame)
                    stream.flush()
                    time.sleep(FRAME_TIMEOUT)
    except Exception as e:
        conn.close()
        print("[EXIT]", addr)
        return

def goodbye():
    stop_event.set()
    sock.close()
    print("[Goodbye]")
    sys.exit()

sock.listen(5)

while True:
    try:
        conn, addr = sock.accept()
        print("[JOIN]", addr)
        threading.Thread(target=proccess_user, args=(conn, addr,)).start()
    except: sys.exit()


# COPYRIGHT 2025 (C) Ali Al-mayahi 