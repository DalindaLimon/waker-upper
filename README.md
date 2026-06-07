Waker-Upper script

Waker-Upper script allows you to use your computer as a remotely triggered alarm. The application runs on the PC you want to use as the alarm and listens for incoming trigger requests on your local network.

When triggered, Waker-Upper script automatically opens a configured YouTube URL and gradually increases the volume of the selected audio device, making it ideal for wake-up alarms, notifications, and automation projects.

Setup
Install and run Waker-upper script on the computer you want to use as the alarm.
Configure the application's local IP address using the PC's Ethernet or Wi-Fi IP address. (Line 38)
Configure the YouTube URL and audio output device.
Start the server.

Example:

local_ip= "192.168.1.100"

Use the local network IP of the computer running Waker-Upper script.

Usage

Once waker-upper script is running, simply send a trigger request to the configured IP address from another device on the network.

When a trigger is received, Waker-upper script will:

Open the configured YouTube video.
Route audio through the selected output device.
Gradually increase the volume over time.
Features
Remote network triggering.
Custom YouTube alarm videos.
Gradual volume increase.
Configurable audio output device.
Simple local network setup.
Use Cases
Remote wake-up alarms.
Smart home automations.
Network-triggered notifications.
Custom alert systems.
