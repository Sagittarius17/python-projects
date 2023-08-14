import time
from datetime import datetime as dt

# Hosts file location (use the correct path based on your OS)
# hosts_path = "/etc/hosts"  # Linux & MacOS
hosts_path = r"C:/Windows/System32/drivers/etc/hosts"  # Uncomment for Windows

redirect_ip = "127.0.0.1"
websites_to_block = ["www.shuvendusingha.onrender.com", "shuvendusingha.onrender.com"]  # List of websites you want to block

while True:
    # For this example, we'll block websites from 8 AM to 4 PM. You can change this accordingly.
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in websites_to_block:
                if website not in content:
                    file.write(redirect_ip + " " + website + "\n")
    else:
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_to_block):
                    file.write(line)
            file.truncate()

    time.sleep(60*5)  # Check every 5 minutes
