import random
import os
import requests

api = "https://cloudflare-eth.com"

payload = {
    "jsonrpc": "2.0",
    "method": "eth_getBalance",
    "params": ["0x20B8869237ab9eCd34bA9d1640C35e925C56f51C", "latest"],
    "id": 1
}

res = requests.post(api, json=payload)
data = res.json()

if "error" in data:
    recipientbal = 0
else:
    wei = int(data["result"], 16)
    recipientbal = wei / 10**18

key = "0x"
characters = "0123456789abcdef"
recipient = "0x20B8869237ab9eCd34bA9d1640C35e925C56f51C"

while len(key) < 40:
    char = random.choice(characters)
    if char.isalpha() and random.random() < 0.5:
        char = char.upper()
    key += char

balance = 100

def main():
    global balance, recipientbal
    os.system("cls")
    print(f"Your wallet (£{balance}):")
    print(key)
    print(f"\n{'£':>44}{balance}\n")
    print(f"{"Amount to pay":^100}\n")
    print(f"Recipient wallet (£{recipientbal}):")
    print(recipient)
    while True:
        choice = input("\n> ")
        if choice.strip() == "":
            main()
        try:
            amount = int(choice)
            if amount <= balance:
                balance -= amount
                recipientbal += amount
                main()
            else:
                main()
        except ValueError:
            main()

main()
