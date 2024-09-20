# Python-system-info
This Python script collects and displays key system information including details about the operating system, CPU usage, RAM usage, local IP address, and battery status (if applicable). The program leverages the psutil, platform, and socket libraries to provide a snapshot of your system's current performance metrics.
Features:
Operating System Detection: Identifies the operating system your machine is running (e.g., Windows, Linux, macOS).
CPU Usage: Shows the current CPU usage as a percentage.
RAM Usage: Displays the current RAM usage percentage.
Local IP Address: Fetches the local IP address of the machine.
Battery Information: If the system has a battery (like a laptop), the script displays the battery percentage and whether the system is plugged into a power source.
Prerequisites:
Before running the script, ensure the following libraries are installed:

bash
Copy code
pip install psutil
