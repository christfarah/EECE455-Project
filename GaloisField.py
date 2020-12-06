import numpy as np


def GH(x):
    # Returns Galois prime polynomial hex representation,ex: 2^8 -> 0x1B
    galois_hex = {
        8: (0x11B),
        7: (0x83),
        6: (0x43),
        5: (0x25),
        4: (0x19),
        3: (0x0D),
        2: (0x07)
    }
    return galois_hex[x]


def strbin2bin(x):
    return "0b" + x


def strhex2hex(x):
    return "0x" + x


def hex2bin(x):
    return bin(hex2dec(x))


def bin2hex(x):
    return hex(int(x, 2))


def hex2dec(x):
    return int(x, 16)


def dec2hex(x):
    return hex(x)


def FindDegree(v):
    if (v):
        result = -1
        while (v):
            v = v >> 1
            result = result + 1
        return result
    else:
        return 0


def ShowPolynomial(f):
    f = hex2dec(f)
    fDegree = FindDegree(f)
    result = ''

    if (f == 0):
        return '0'

    for i in range(fDegree, 0, -1):
        if ((1 << i) & f):
            result = result + (' x^' + repr(i))
    if (1 & f):
        result = result + ' ' + repr(1)

    return result.strip().replace(' ', ' + ')


# NEEDS MODULO IMPLEMENTATION
def Add(x, y, mod):
    x = hex2dec(x)
    y = hex2dec(y)

    """
    Adds two field elements and returns the result.
    """

    res = moduloreduction(hex(x ^ y), mod)

    return res


def moduloreduction(a, mod):
    b = dec2hex(GH(mod))
    a = hex2bin(a)[2:]
    b = hex2bin(b)[2:]
    x = []
    y = []

    for i in range(len(a)):
        x.append(int(a[i]))

    for i in range(len(b)):
        y.append(int(b[i]))

    del i
    list = np.polydiv(x, y)
    remainder = list[1] % 2

    temp = remainder
    remainder = "0b"
    for i in range(len(temp)):
        remainder = remainder + (temp[i].astype(np.int64)).astype(np.str)
    del temp

    return bin2hex(remainder)


def Subtract(x, y, mod):
    return Add(x, y, mod)


def Invert(a, mod):
    d, x, y = p_egcd(int(hex2bin(a), base=2), GH(mod))
    return dec2hex(x)


def Multiplication(a, b, mod):
    a = hex2bin(a)[2:]
    b = hex2bin(b)[2:]
    x = []
    y = []

    for i in range(len(a)):
        x.append(int(a[i]))

    for i in range(len(b)):
        y.append(int(b[i]))

    del i
    list = np.polymul(x, y)
    res = list % 2

    # Array to binary representation
    temp = res
    res = "0b"
    for i in range(len(temp)):
        res = res + (temp[i].astype(np.int64)).astype(np.str)
    del temp

    res = moduloreduction(bin2hex(res), mod)

    return res


def Division(a, b, mod):
    a = hex2bin(a)[2:]
    b = hex2bin(b)[2:]
    x = []
    y = []

    for i in range(len(a)):
        x.append(int(a[i]))

    for i in range(len(b)):
        y.append(int(b[i]))

    del i
    list = np.polydiv(x, y)
    quotient = list[0] % 2

    # Array to binary representation
    temp = quotient
    quotient = "0b"
    for i in range(len(temp)):
        quotient = quotient + (temp[i].astype(np.int64)).astype(np.str)
    del temp

    quotient = moduloreduction(bin2hex(quotient), mod)

    return quotient


def p_divmod(a, b):
    """ Binary polynomial division.
        Divides a by b and returns resulting (quotient, remainder) polynomials.
        Precondition: b != 0 """
    q = 0;
    bl = b.bit_length()
    while True:
        shift = a.bit_length() - bl
        if shift < 0: return (q, a)
        q ^= 1 << shift;
        a ^= b << shift


def p_egcd(a, b):
    a = (a, 1, 0)
    b = (b, 0, 1)
    while True:
        q, r = p_divmod(a[0], b[0])
        if not r: return b
        a, b = b, (r, a[1] ^ p_mul(q, b[1]), a[2] ^ p_mul(q, b[2]))


def p_mul(a, b):
    result = 0
    while a and b:
        if a & 1: result ^= b
        a >>= 1;
        b <<= 1
    return result
