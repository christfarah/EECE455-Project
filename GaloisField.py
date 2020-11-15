import numpy as np

def GH(x):
    # Returns Galois prime polynomial hex representation,ex: 2^8 -> 0x1B
    galoishex = {
        8: (0x1B),
        7: (0x83),
        6: (0x43),
        5: (0x25),
        4: (0x19),
        3: (0x0D),
        2: (0x07)
    }

    return (galoishex[x])


def hex2bin(x):
    return bin(hex2dec(x))


def bin2hex(x):
    return hex(int(x, 2))


def hex2dec(x):
    return int(x, 16)


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
def Add(x, y):
    x = hex2dec(x)
    y = hex2dec(y)

    """
    Adds two field elements and returns the result.
    """

    return hex(x ^ y)


def mod(x, mod):
    x = hex2bin(x)
    y = ""
    for i in range(mod):
        y += x[len(x) - 1 - i]
    return bin2hex(y[::-1])


def Subtract(x, y):
    """
    Subtracts the second argument from the first and returns
    the result.  In fields of characteristic two this is the same
    as the Add method.
    """
    return Add(x, y)


def Invert(a, mod):
    a = hex2dec(a)
    v = GH(mod)
    g1 = 1
    g2 = 0
    j = FindDegree(a) - mod
    while (a != 1):
        if (j < 0):
            a, v = v, a
            g1, g2 = g2, g1
            j = -j

        a ^= v << j
        g1 ^= g2 << j

        a %= pow(2, mod)  # Emulating n-bit overflow
        g1 %= pow(2, mod)  # Emulating n-bit overflow

        j = FindDegree(a) - FindDegree(v)

    return hex(g1)


def Multiplication(a, b, mod):
    a = hex2dec(a)
    b = hex2dec(b)
    p = 0
    for i in range(mod):
        if (b & 1) != 0:
            p ^= a

        high_bit_set = a & hex2dec(hex(pow(2, mod - 1)))
        a <<= 1
        if high_bit_set != 0:
            a ^= GH(mod)
            a = a % pow(2, mod)  # Emulating n-bit overflow
        b >>= 1
    return hex(p)

def Division(a, b, mod):
    a = hex2bin(a)
    b = hex2bin(b)
    x=[]
    y=[]
    temp_x=a[::-1]
    temp_y=b[::-1]

    for i in range(len(temp_x) - 2):
        x.append(int(temp_x[i]))

    for i in range(len(temp_y) - 2):
        y.append(int(temp_y[i]))

    del temp_x,temp_y,i
    list=np.polydiv(x,y)
    quotient = list[0]%2
    remainder= list[1]%2

    # Array to binary representation
    temp=quotient
    quotient="0b"
    for i in range(len(temp)):
        quotient=quotient+(temp[i].astype(np.int64)).astype(np.str)
    del temp

    temp=remainder
    remainder="0b"
    for i in range(len(temp)):
        remainder=remainder+(temp[i].astype(np.int64)).astype(np.str)
    del temp

    quotient=bin2hex(quotient)
    remainder=bin2hex(remainder)
    # QUOTIENT AND REMAINDER IS AVAILABLE IN HEX
    # DELETE THIS PRINT AFTER TESTING
    print("Quotient: ",ShowPolynomial(quotient),"\n")
    print("Remainder: ",ShowPolynomial(remainder),"\n")

    res=[quotient,remainder]
    return res
