import hashlib
import random


t = 5


def getHash(s):
    for i in range(0, t):
        hs = hashlib.md5()
        hs.update(s.encode('utf-8'))
        s = hs.hexdigest()
    return s


def IsHashEqual(s1, s2):
    m1 = getHash(s1)
    m2 = getHash(s2)
    return m1 == m2
