import subprocess
import os
import traceback

try:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    print("Script started")

    # Disk Check
    disk = subprocess.run(
        "wmic logicaldisk get size,freespace,caption",
        capture_output=True,
        text=True,
        shell=True
    )

    # Network Check
    ping = subprocess.run(
        ["ping", "-n", "4", "google.com"],
        capture_output=True,
        text=True
    )

    # Save Output
    with open("output.txt", "w") as f:
        f.write(disk.stdout)
        f.write(ping.stdout)

except Exception as e:
    with open("error_log.txt", "w") as f:
        f.write(str(e) + "\n")
        f.write(traceback.format_exc())

print("Auto trigger test")