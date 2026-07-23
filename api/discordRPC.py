from pypresence import Presence
import time

CLIENT_ID = "1529861003880304692"

RPC = Presence(CLIENT_ID)
RPC.connect()

RPC.update(
    details="Follow me on GitHub",
    state="https://github.com/Charlie-Edwards",
    start=int(time.time()),
)

while True:
    pass
