# Waker-Upper Script

Waker-Upper Script lets you use your computer as a remotely triggered alarm.

Run the script on the PC you want to act as the alarm. When the script receives a trigger request from another device on your network, it automatically opens a YouTube video and gradually increases the volume of your selected audio device.

Perfect for wake-up alarms, notifications, and home automation projects.

## Setup

1. Download and run Waker-Upper Script on the computer you want to use as the alarm.
2. Open the script and set your computer's local IP address on **Line 38**.
3. Set the YouTube URL you want to play when the alarm is triggered.
4. Select the audio output device (speakers, headphones, etc.).
5. Start the script.

### Example

```python
local_ip = "192.168.1.100"
```

Use the local Ethernet or Wi-Fi IP address of the computer running Waker-Upper Script.

## Usage

After the script is running, simply send a trigger request to the configured IP address from another device on the same network.

When a trigger is received, Waker-Upper Script will:

* Open the configured YouTube video.
* Play audio through the selected output device.
* Gradually increase the volume over time.

## Features

* Remote network triggering
* Custom YouTube alarm videos
* Gradual volume increase
* Configurable audio output device
* Simple local network setup

## Use Cases

* Remote wake-up alarms
* Smart home automation
* Network-triggered notifications
* Custom alert systems
* Remote audio announcements
