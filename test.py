import secp256k1
import hashlib
from binascii import hexlify
import time
import uasyncio
import _thread

secret = hashlib.sha256(b"secret key").digest()[:-8]
secretx = hashlib.sha256(b"secret key").digest()
print("Secret key:", hexlify(secretx).decode())
time.sleep(1)
print("Secret key:", hexlify(secret).decode())
time.sleep(0.1)

async def crash():
    try:
        if not secp256k1.ec_seckey_verify(secret):
            print("ERRORRORORORORO")
    except Exception as e:
        print(e)

async def start():
    print("starting")
    time.sleep(1)
    try:
        await uasyncio.wait_for(crash(), 10)
    finally:
        print("timeout ended")

print("main indentity", _thread.get_ident()) # 537106508
def _main():
    print("indentity", _thread.get_ident()) # 536926912
    uasyncio.run(start())

thread = _thread.start_new_thread(_main, ())
print("thread started")
time.sleep(10)
print("ending thread from main")
