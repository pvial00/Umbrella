import random
from Crypto.Util import number
from Crypto.Random import random as prandom
import math

# requires pycrypto

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

def testencrypt(pk, sk, mod):
    msg = "012345678901234567890"
    msg = "H"
    m = number.bytes_to_long(msg)
    ctxt = encrypt(m, pk, mod)
    if sk != None:

        ptxt = decrypt(ctxt, sk, mod)
        if ptxt == m:
            return True
        else:
            return False
    return Falses

#def genBasePrimes(psize):
#    p = number.getPrime(psize)
#    q = number.getPrime(psize)
#    while q == p:
#        q = number.getPrime(psize)
#    return p, q

def genBasePrimes(psize):
    p = number.getPrime(psize)
    q = number.getPrime(psize)
    while q == p:
        q = number.getPrime(psize)
    return p, q

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

text = "A"
msg = number.bytes_to_long(text)
print msg
sk, pk, mod, t, p, q =  keygen(8)
print sk, pk, mod
ctxt = encrypt(msg, pk, mod)
print ctxt
ptxt = decrypt(ctxt, sk, mod)
print ptxt
if ptxt != msg:
    print "Key is broken"
    exit(1)

import math
crack = int(math.sqrt(math.sqrt(mod)))
print "crack", crack

primes = []
ceiling = 500000
start = 1
inc = 1
for i in range(start, ceiling, inc):
#for i in range(crack, 6500, 1):
    #print i, mod % i
    #if i == t:
    #    print mod & i
    #if i == s:
    #    print mod & i
    #if i == l:
    #    print mod & i
    try:
        if (mod % i) == 0 and i >= 1:
            primes.append(i)
    except ZeroDivisionError as zer:
        pass

print primes
print "Modulus sanity check"
sk2 = number.inverse(pk, mod)
print sk2
tmp = decrypt(ctxt, sk2, mod)
if tmp == msg:
    print "Cracked", tmp
    exit(0)
print "Modulus - 1 sanity check"
sk2 = number.inverse(pk, (mod - 1))
print sk2
tmp = decrypt(ctxt, sk2, mod)
if tmp == msg:
    print "Cracked", tmp
    exit(0)
print "mod mod P"
print mod % p
print "mod mod Q"
print mod % q
print "mod mod T"
print mod % t
print "Solve with P and Q but the question is how to identify P and Q"
ps = ((p - 1) * (q - 1))
sk2 = number.inverse(pk, ps)
print sk2
print decrypt(ctxt, sk2, mod)
print "p, q"
print p, q
print primes
print "This should always decrypt"
sk2 = number.inverse(pk, t)
print sk2
print decrypt(ctxt, sk2, mod)


print "Crack from primes"
#if primes[len(primes)-1] == mod:
#for i in range(5):
#    primes.pop()
p2 = primes.pop()
q2 = primes.pop()  -1
print p2, q2
#exit(0)
s = ((p2 - 1) * (q2 - 1))
sk2 = number.inverse(pk, s)
tmp = decrypt(ctxt, sk2, mod)
if tmp == msg:
    print "Cracked", tmp
    exit(0)
print "Solve with P and Q but the question is how to identify P and Q"
ps = ((p - 1) * (q - 1))
sk2 = number.inverse(pk, ps)
print sk2
print decrypt(ctxt, sk2, mod)
print "p, q"
print p, q
print primes
print "This should always decrypt"
sk2 = number.inverse(pk, t)
print sk2
print decrypt(ctxt, sk2, mod)


print "Crack with P"
sk2 = number.inverse(pk, (p-1))
tmp = decrypt(ctxt, sk2, mod)
if tmp == msg:
    print "Cracked", tmp
    #exit(0)
print "Crack with Q"
sk2 = number.inverse(pk, (q-1))
tmp = decrypt(ctxt, sk2, mod)
if tmp == msg:
    print "Cracked", tmp
    #exit(0)
print "Reddit santiy check"
s = ((mod) * 2) 
#s = (((p - 1) * mod) * ((q - 1) * mod))
sk2 = number.inverse(pk, s)
tmp = decrypt(ctxt, sk2, mod)
if tmp == msg:
    print "Cracked", tmp
    #exit(0)
print "Check 2"
p2 = 2
q2 = mod / p2
s = ((p2 - 1) * (q2 - 1))
print s
sk2 = number.inverse(pk, s)
tmp = decrypt(ctxt, sk2, mod)
if tmp == msg:
    print "Cracked", tmp
    exit(0)
print "Cracking with Fermat"
p2 = fermat(mod)
q2 = mod / p2
t = ((p2 - 1) * (q2 - 1))
sk2 = number.inverse(pk, t)
tmp = decrypt(ctxt, sk2, mod)
if tmp == msg:
    print "Cracked", tmp
    #exit(0)
