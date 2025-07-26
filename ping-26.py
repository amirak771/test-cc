import ipaddress
import subprocess
import platform

def ping(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '2', host]
    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

# Create the network
network = ipaddress.ip_network('172.19.0.0/24', strict=False)

# Iterate through all hosts in the network
for ip in network.hosts():
    ip_str = str(ip)
    if ping(ip_str):
        print(f"{ip_str} is reachable")
    else:
        print(f"{ip_str} is not reachable")
