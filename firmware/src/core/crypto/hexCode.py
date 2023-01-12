import binascii
import hashlib

def hex_to_checksum(input: list[str]):
    chunks = [int("".join((input + ["0"])[i:i+3]), 16) for i in range(0,36,3)]
    binary = "".join(["{0:012b}".format(chunk)[1:] for chunk in chunks])[:128]
    bytes = int(binary, 2).to_bytes(16, "big")
    sha = hashlib.sha256(bytes).digest()
    hex = binascii.hexlify(sha)
    checksum = hex.decode()[0].upper()
    return checksum
    