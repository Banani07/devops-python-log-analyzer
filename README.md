# 🚀 DevOps Python Toolkit

## 📌 Overview

This project demonstrates my hands-on learning journey in DevOps using Python.
It includes scripts for **log analysis** and **system monitoring**, simulating real-world DevOps tasks like debugging, validation, and health checks.

---

## 📘 Day 1 - Basic Log Analyzer

### 🔹 Description

A simple Python script to read a log file and count the number of `ERROR` and `INFO` messages.

### 🔹 Key Concepts

* File handling (`with open`)
* Loops and conditions
* String matching
* Basic Git commands

### 🔹 Sample Code

```python
with open("log.txt", "r") as file:
    error_count = 0
    info_count = 0

    for line in file:
        if "ERROR" in line:
            error_count += 1
        elif "INFO" in line:
            info_count += 1

print("ERROR:", error_count)
print("INFO:", info_count)
```

---

## 📘 Day 2 - Advanced Log Analyzer

### 🔹 Description

Enhanced the log analyzer to handle multiple log levels, calculate error percentage, and implement alerting.

### 🔹 Features

* Handles `ERROR`, `INFO`, `WARNING`
* Case-insensitive log detection
* Calculates error percentage
* Handles empty file and missing file
* Alert system for high error count

### 🔹 Sample Code

```python
try:
    log_counts = {
        "error": 0,
        "info": 0,
        "warning": 0
    }

    total_lines = 0

    with open("log.txt", "r") as file:
        for line in file:
            total_lines += 1
            line = line.lower()

            for key in log_counts:
                if key in line:
                    log_counts[key] += 1

    if total_lines == 0:
        print("Log file is empty.")
    else:
        error_percentage = (log_counts["error"] / total_lines) * 100

        print("\n--- Log Summary ---")
        for key, value in log_counts.items():
            print(f"{key.upper()}: {value}")

        print("Total lines:", total_lines)
        print("Error %:", round(error_percentage, 2))

        if log_counts["error"] > 5:
            print("ALERT: High error rate detected!")

except FileNotFoundError:
    print("Log file not found.")
```

---

## 📘 Day 3 - System Monitoring Script

### 🔹 Description

A Python-based system monitoring tool that executes system commands to check disk usage and network connectivity.

### 🔹 Features

* Runs system commands using subprocess
* Displays disk information
* Checks network connectivity using ping
* Alerts if network issue detected

### 🔹 Sample Code

```python
import subprocess

print("=== SYSTEM MONITOR ===\n")

# Disk Check
disk = subprocess.run(
    "wmic logicaldisk get size,freespace,caption",
    capture_output=True,
    text=True,
    shell=True
)

print("Disk Info:\n", disk.stdout)

# Network Check
ping = subprocess.run(
    ["ping", "google.com"],
    capture_output=True,
    text=True
)

print("\nNetwork Status:\n", ping.stdout)

# Alert Logic
if "TTL=" not in ping.stdout:
    print("\nALERT: Network issue detected!")
else:
    print("\nNetwork is working fine")
```

---

## 🛠 Tech Stack

* Python
* Git
* GitHub

---

## 🚀 How to Run

1. Clone the repository

```
git clone <your-repo-link>
```

2. Navigate to project folder

```
cd devops-python
```

3. Run scripts

```
python script.py
python system_check.py
```

---

## 💼 Real-World Use Cases

* Log monitoring after deployment
* Detecting application failures
* System health monitoring
* Basic automation for DevOps workflows

---

## 🧠 Key Learnings

* Python scripting for automation
* Log parsing and analysis
* Running system commands
* Error handling and edge cases
* Version control using Git

---

## 🚧 Future Enhancements

* Add CPU and memory monitoring
* Schedule scripts using cron/Task Scheduler
* Integrate alerting (email/Slack)
* Improve log parsing with regex

---

## 🙌 Author

Banani Manna
