import requests
from bs4 import BeautifulSoup
import os
import random

proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050',
    'http': 'socks5h://127.0.0.1:9150',
    'https': 'socks5h://127.0.0.1:9150'
}

url = 'https://check.torproject.org/'

uagent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

splash = [
    "Export as html? (type /html)",
    "'google' -> https://google.com",
    ".onion links are supported"
]

try:
    response = requests.get(url, proxies=proxies, headers=uagent)
except:
    response = requests.get(url, headers=uagent)

torcheck = BeautifulSoup(response.text, 'html.parser')

try:
    os.system("cls")
except:
    os.system("clear")

print(f"{torcheck.find('h1').text[12:].replace('\n', '').rstrip()}")
print(f"Your IP address appears to be: {torcheck.find('strong').text}")
print("\nSearch anything (eg: 'google', 'check.torproject.org'\n"
    "                 or: 'http://2gzyxa5ihm7nsggfxnu52rck2vv4rvmdlkiu3zzui5du4xyclen53wid.onion')\n")

def search():

    global src

    while True:

        q = input("Enter site: ")

        if q == "/html":
            try:
                export(recent)
            except UnboundLocalError:
                print("\nEnter a site before you export it\n")
        else:

            if q[:4] != "http":
                q = f"http://{q}".rstrip()
            else:
                q.rstrip()

            if "." not in q:
                q = f"{q}.com"
            else:
                pass

            try:
                r = requests.get(q, headers=uagent, proxies=proxies)
            except:
                r = requests.get(q, headers=uagent)

            bs = BeautifulSoup(r.text, 'html.parser')

            try:
                os.system("cls")
            except:
                os.system("clear")

            src = bs.prettify()

            print(src)
            recent = q

            try:
                response = requests.get(url, proxies=proxies, headers=uagent)
            except:
                response = requests.get(url)

            torcheck = BeautifulSoup(response.text, 'html.parser')

            print(f"{torcheck.find('h1').text[12:].replace('\n', '').rstrip()}", end=' ')
            print(f"({random.choice(splash)})\n")

def export(recent):

    recent = recent.split("/")[2]

    with open(f"{recent}.html", "w") as f:
        f.write(f"{src}")

    print(f"\nExported as html!\n")

    search()

search()
