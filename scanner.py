import socket

target = input("Enter target IP: ")

try:
    socket.inet_aton(target)
except socket.error:
    print("Invalid IP address.")
    exit()

try:
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
except ValueError:
    print("Ports must be numbers.")
    exit()

if start_port < 1 or end_port > 65535 or start_port > end_port:
    print("Invalid port range.")
    exit()

print(f"\nScanning target: {target}")
print(f"Port Range: {start_port} - {end_port}")
print("-" * 30)

open_ports = 0

for port in range(start_port, end_port + 1):

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