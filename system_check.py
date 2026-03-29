import subprocess

print("=== SYSTEM MONITOR ===\n")

# 🔹 1. Disk Check (Windows)
disk = subprocess.run(
    "wmic logicaldisk get size,freespace,caption",
    capture_output=True,
    text=True,
    shell=True
)

print("💾 Disk Info:\n")
print(disk.stdout)

# 🔹 2. Network Check
ping = subprocess.run(
    ["ping", "google.com"],
    capture_output=True,
    text=True
)

print("\n🌐 Network Status:\n")
print(ping.stdout)

# 🔹 3. Alert Logic
if "TTL=" not in ping.stdout:
    print("\n🚨 ALERT: Network issue detected!")
else:
    print("\n✅ Network is working fine")
print(type(disk))
print("System check completed")