import psutil
import platform
import socket

def get_system_info():
    """Gathers system information and returns it as a dictionary."""

    info = {}
    info['os'] = platform.system()  # Gets the operating system (e.g., Windows, Linux, macOS)
    info['cpu'] = psutil.cpu_percent()  # Gets the current CPU usage in percentage
    info['ram'] = psutil.virtual_memory().percent  # Gets the current RAM usage in percentage
    info['ip_address'] = socket.gethostbyname(socket.gethostname())  # Gets the local IP address

    # Battery information (if applicable)
    try:
        info['battery'] = psutil.sensors_battery()
        info['battery_percent'] = info['battery'].percent
        info['battery_plugged'] = info['battery'].plugged
    except Exception:
        info['battery'] = None

    return info

if __name__ == "__main__":
    system_info = get_system_info()
    print(system_info)