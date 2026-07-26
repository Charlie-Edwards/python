import json
import sys
import os
import platform
import websocket
import keyboard
import numpy as np
import colorama

WS_URL = "wss://advanced-trade-ws.coinbase.com"

bal = None
trading = False
last_space = False
price = 0
entryprice = 0
sign = ""

while bal == None:
    try:
        with open("wallet.txt", "r") as f:
            oldbal = float(f.read())
            bal = oldbal
    except:
        with open("wallet.txt", "w") as f:
                f.write("100")

if platform.system().lower().startswith("windows"):
    clear = "cls"
elif platform.system().lower().startswith("linux"):
    clear = "clear"
else:
    clear = "clear"

colorama.init()

def save(balance):
    with open("wallet.txt", "w") as f:
        f.write(str(balance))

def on_open(ws):
    ws.send(json.dumps({
        "type": "subscribe",
        "product_ids": ["SOL-USD"],
        "channel": "ticker"
    }))

def on_message(ws, message):
    global bal, trading, last_space, price, entryprice

    data = json.loads(message)

    for event in data.get("events", []):
        for ticker in event.get("tickers", []):
            price = float(ticker["price"])

    if price is None:
        return

    space = keyboard.is_pressed("space")
    if space and not last_space:
        trading = not trading
        if trading:
            entryprice = price
        else:
            bal += (price - entryprice)
            save(bal)
    last_space = space

    os.system(clear)
    if not trading:
        if np.sign((bal - oldbal)) == -1:
            sign = ""
            signcolor = colorama.Fore.LIGHTRED_EX
        else:
            sign = "+"
            signcolor = colorama.Fore.LIGHTGREEN_EX
        print(f"SOLUSD: ${price:.2f} | Balance: ${bal:.2f} | P&L: {signcolor}{sign}{(bal - oldbal):.2f}${colorama.Fore.RESET}")
        print(f"{"\n"*3}{colorama.Fore.LIGHTGREEN_EX}Buy 1 SOL (hold [SPACE]){colorama.Fore.RESET}{"\n"*10}")
    else:
        if np.sign((price - entryprice)) == -1:
            sign = ""
            signcolor = colorama.Fore.LIGHTRED_EX
        else:
            sign = "+"
            signcolor = colorama.Fore.LIGHTGREEN_EX
        print(f"SOLUSD: ${price:.2f} | Balance: ${bal:.2f}")
        print(f"Open: {entryprice:.2f} | Close: {price:.2f} | P&L: {signcolor}{sign}{(price - entryprice):.2f}${colorama.Fore.RESET}")
        print(f"{"\n"*2}{colorama.Fore.LIGHTRED_EX}Sell 1 SOL (hold [SPACE]){colorama.Fore.RESET}{"\n"*10}")
    print(f"See this chart on tradingview: https://www.tradingview.com/chart/p5P8IAsQ/?symbol=SOLUSD")
    print(f"Donations: ScKMr5MANt3RSGgwWv4Kot22ETKtSA4y5hc3Db3Qx66", end="", flush=True)

ws = websocket.WebSocketApp(
    WS_URL,
    on_open=on_open,
    on_message=on_message
)

try:
    ws.run_forever()
except KeyboardInterrupt:
    save(bal)
