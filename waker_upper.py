from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess
import webbrowser
import threading
import asyncio
import socket

class Handler(BaseHTTPRequestHandler):
    async def volup():
        subprocess.run(["nircmd.exe", "changesysvolume", "-65535"])
        for i  in range(32):
         subprocess.run(["nircmd.exe", "changesysvolume", "2000"])
         await asyncio.sleep(2)


    def do_GET(self):
        if self.path == '/trigger':
            # Switch to speakers (you might want to change this)
            subprocess.run(["nircmd.exe", "setdefaultsounddevice", "Speakers"])
            
            
            # Open URL (you can change this to your desired url)
            webbrowser.open("https://youtu.be/XfqOB4hvxlY" + "&autoplay=1")
            threading.Thread(
                target=lambda: asyncio.run(Handler.volup()),
                daemon=True
            ).start()
            # Send response
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Success!")

        else:
            self.send_response(404)
            self.end_headers()

# Start server on port 8888 on local ip
local_ip =  #this should be your local ip
server = HTTPServer((local_ip, 8888), Handler)
print("Server running on "+ local_ip + ":8888")
server.serve_forever()