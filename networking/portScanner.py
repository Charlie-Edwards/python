import socket
import nmap
import os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
n = nmap.PortScanner()

s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]

ports = [22, 25, 80, 443, 587, 993, 995, 3389, 5900]

for l in os.popen("netstat -ano | findstr LISTENING"):
    address = l.split()[1]
    port = int(address.rsplit(":", 1)[1])
    ports.append(port)

ports = sorted(set(ports))

for port in ports:
    print(f"Scanning: {ip}:{port}")

for port in ports:
    result = n.scan(ip, str(port))
    status = (result['scan'][ip]['tcp'][port]['state'])
    print(f"Port {port} is {status}")
