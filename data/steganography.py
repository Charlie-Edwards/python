file = input("File: ")

end_hex = b"\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82"

if file.endswith("png"):
    with open(file, 'rb') as f:
        content = f.read()
        offset = content.index(end_hex)
        f.seek(offset + len(end_hex))
        hiddenbytes = f.read()
        hiddentext = hiddenbytes.decode("utf-8")

if file.endswith("jpg"):
    with open(file, 'rb') as f:
        content = f.read()
        offset = content.index(bytes.fromhex('FF D9'))
        f.seek(offset + 2)
        hiddenbytes = f.read()
        hiddentext = hiddenbytes.decode("utf-8")

print("--- Hidden text ---")
print(hiddentext)
print("-------------------")
print(" ".join(f"{b:02X}" for b in hiddenbytes))
