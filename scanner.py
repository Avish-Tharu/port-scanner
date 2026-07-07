import socket

target = input("Enter target IP: ")

start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

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