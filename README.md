# ASCII Video Streaming Server

This is a **Python-based TCP server** that streams **animated ASCII videos** over a socket connection. Inspired by `parrot.live`, this server reads frames from a folder and continuously sends them to connected clients, such as `curl`.

## Features
- Streams ASCII animations via a simple TCP server.
- Supports **colorful** frames with ANSI escape codes.
- Uses **multi-threading** to handle multiple clients simultaneously.
- Loads frames dynamically from a specified folder.
- Configurable settings via `config.json`.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Alicrafty1191/LiveServer.git
   cd LiveServer
   ```
2. Install required dependencies (Python 3 is required):
   ```bash
   pip install -r requirements.txt  # If applicable
   ```

## Usage

1. Prepare a folder named `frames/` and place ASCII frames inside (e.g., `0.txt`, `1.txt`, `2.txt`, ...).
2. Run the server:
   ```bash
   python server.py
   ```
3. Connect to the server using `curl`:
   ```bash
   curl -N http://your-server-ip:777
   ```
   Replace `your-server-ip` with the actual IP address.

## Configuration
Edit `config.json` to customize settings:
```json
{
  "FRAMES_FOLDER_PATH": "./frames",
  "FRAME_TIMEOUT": 0.5,
  "IP_ADDRESS": "0.0.0.0",
  "PORT": 777,
  "COLORFUL": true,
  "FRAMES": 10
}
```
- `FRAME_TIMEOUT`: Time delay between frames (in seconds).
- `COLORFUL`: If `true`, frames will be sent with random ANSI colors.

## Example Frame (`frames/0.txt`)
```
  (\_/)
 ( o.o )
 >  ^  
```

## License
**Copyright © 2025 Ali Al-mayahi**

This project is licensed under the MIT License. Feel free to use and modify it as needed.

## Author
- **Ali Al-mayahi**
- [YouTube](https://youtube.com/@ali_crafty)
- [TikTok](https://www.tiktok.com/@tr6s_)
- [Instagram](https://www.instagram.com/tr6s.i)
- [Facebook](https://www.facebook.com/profile.php?id=100078004273350)

Enjoy ASCII animations! 🚀

