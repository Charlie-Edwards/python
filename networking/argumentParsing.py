import sys
import nmap
import time
import random

nmap = nmap.PortScanner()

fakewait = random.randint(1, 4000) / 1000

if len(sys.argv) > 2:

    print(f"sudo nmap {sys.argv[1]} {sys.argv[2]}")

    if sys.argv[1] == "-sn":
        print(f"Starting Nmap 3.301 ( https://nmap.org ) at {time.ctime()}")
        results = nmap.scan(sys.argv[2], arguments=sys.argv[1])

        for host in nmap.all_hosts():
            print(f'Nmap scan report for {host}')
            print(f'Host is {nmap[host].state()} (1.337s latency).')
            print(f"MAC Address: {nmap[host]['addresses'].get('mac', 'Unknown')} ({nmap[host]['vendor'].get(nmap[host]['addresses'].get('mac', 'Unknown'), 'Unknown')})")

        elapsed = results['nmap']['scanstats']['elapsed']
        up = results['nmap']['scanstats']['uphosts']

        print(f"Nmap done: 256 IP addresses ({up} hosts up) scanned in {elapsed} seconds")

    else:
        time.sleep(fakewait)
        print("Sorry, but only a '-sn' scan can be done.")

else:
    time.sleep(fakewait)
    print("Invalid arguments. (eg: 'argumentParsing.py -sn 192.168.0.0/24')")
