# Python-system-info
This Python script collects and displays key system information including details about the operating system, CPU usage, RAM usage, local IP address, and battery status (if applicable). The program leverages the psutil, platform, and socket libraries to provide a snapshot of your system's current performance metrics.
Features:
Operating System Detection: Identifies the operating system your machine is running (e.g., Windows, Linux, macOS).
CPU Usage: Shows the current CPU usage as a percentage.
RAM Usage: Displays the current RAM usage percentage.
Local IP Address: Fetches the local IP address of the machine.
Battery Information: If the system has a battery (like a laptop), the script displays the battery percentage and whether the system is plugged into a power source.
Prerequisites:
Before running the script, ensure the following libraries are installed or install them using:
pip install psutil

***How to Run:
Clone the repository or download the script.
Run the script in your terminal or command prompt as below:
python3 system_info.py
or run on visual studio code when you install the proper extensions too

you should get something like this:
{
  "os": "Windows",
  "cpu": 10.2,
  "ram": 45.3,
  "ip_address": "192.168.1.10",
  "battery_percent": 90,
  "battery_plugged": True
}

I use Kali LInux so this is what i got:
{'os': 'Linux', 'cpu': 66.7, 'ram': 74.7, 'ip_address': '127.0.1.1', 'battery': None, 'battery_percent': 0.0}

