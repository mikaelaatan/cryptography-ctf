#!/usr/bin/env python3

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from secrets import token_bytes
from os import listdir

key = token_bytes(16)
iv = int.from_bytes(token_bytes(16), byteorder='big')

for filename in listdir():
    print(f'Encrypting {filename}')
    data = open(filename, 'rb').read()

    nonce = int.to_bytes(iv, 16, byteorder='big')
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce))
    aes_enc = cipher.encryptor()
    ctxt = aes_enc.update(data) + aes_enc.finalize()
    
    encfile = open(f'{filename}.enc', 'wb')
    encfile.write(ctxt)
    encfile.close()

    iv += 1

