import socket

target = "127.0.0.1"

print(f"Scanning target: {target}")
print("-" * 30)

for port in range(20, 100):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socket.setdefaulttimeout(0.5)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")

    s.close()

print("-" * 30)
print("Scan completed.")