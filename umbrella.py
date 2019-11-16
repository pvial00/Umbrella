import math
from Crypto.Util import number

# requires pycrypto for prime number generation

def fermat(n):
    from math import sqrt
    x = long(sqrt(n)) + 1
    y = long(sqrt(x**2 - n))
    while True:
        w = x**2 - n - y**2
        if w == 0:
            break
        if w > 0:
            y += 1
        else:
            x += 1
    return x+y

def ZanderTheorem2(n):
    k = 2
    x = long(math.sqrt(n))
    third = (long(math.sqrt(n)) * 2)
    y = (long(math.sqrt(third)) - 1) * k
    while True:
        w = ((x**k - n - y**k) * k) * k
        if w == 0:
            break
        if w > 0:
            y += 1
        else:
            x += 1
        if n % w <= third and w % n > third:
            y += 1
    return x+y

def encrypt(ptxt, pk, mod):
    return pow(ptxt, pk, mod)

def decrypt(ctxt, sk, mod):
    return pow(ctxt, sk, mod)

def sign(ctxt, sk, mod):
    return pow(ctxt, sk, mod)

def verify(ptxt, ctxt, pk, mod, s):
    x = pow(ptxt, pk, mod)
    if x == ctxt:
        return True
    else:
        return False

def keygen(psize):
    p = number.getPrime(psize)
    q = number.getPrime(psize)
    n = ((p%q) + (q%p)) * p * q 
    t = ((p - 1) * (q - 1) * p * q)
    pk = number.getRandomRange(1, t)
    g = number.GCD(pk, t)
    while g != 1:
        pk= number.getRandomRange(1, t)
        g = number.GCD(pk, t)
        if g == 1:
            break
    sk = number.inverse(pk, t)
    return sk, pk, n, t, p, q
