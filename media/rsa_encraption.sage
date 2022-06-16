#!/usr/local/bin/sage

from binascii import hexlify, unhexlify

def rsa_genmodulus(n, e=0x10001):
    while True:
        p = random_prime(2^n-1, lbound=2^(n-1), proof=False)
        q = random_prime(2^n-1, lbound=2^(n-1), proof=False)
        N = p*q
        N_phi = (p-1)*(q-1)
        if gcd(N_phi, e) != 1:
            return N, N_phi, e, p, q
            
def rsa_encrapt(m, N, e):
    return Mod(m, N)^e

def rsa_decrapt(c, N, e, p, q):
    # to-do: implement Algs 1 and 2 from https://eprint.iacr.org/2020/1059.pdf
    raise NotImplementedError

def ascii_to_int(s):
    return int.from_bytes(s, byteorder='big')

def int_to_ascii(i):
    return unhexlify(hex(i)[2:])


if __name__ == '__main__':
    print('Generating keys...')
    N, N_phi, e, p, q = rsa_genmodulus(256, 17)
    print(f'N = {hex(N)}')
    print(f'e = {hex(e)}')
    print(f'phi(N) = {N_phi}')
    print(f'p = {p}')
    print(f'q = {q}')
    
    ptxt = input('\nEnter a string to encrapt: ').encode('utf-8')
    m = ascii_to_int(ptxt)
    assert m < N
    c = rsa_encrapt(m, N, e)
    
    print('\nThe encraption in hex is:')
    print(f'c = {hex(c)}')