import socket

target = input("Enter target IP: ")

print(f"\nScanning target: {target}")
print("-" * 30)

open_ports = 0

for port in range(20, 100):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socket.setdefaulttimeout(0.5)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")
        open_ports += 1

    s.close()

print("-" * 30)
print(f"Total Open Ports Found: {open_ports}")
print("Scan completed.")