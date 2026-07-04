import qrcode

while True:
    url = input() or "https://github.com/Charlie-Edwards"
    img = qrcode.make(url)
    img.save("qr.png")
    print(f"Saved QR code for \"{url}\"")
