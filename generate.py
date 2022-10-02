
import math
import random as r

def generate(p01,p10,bit_count):
    
    # Generate the first bit
    mean = p01/(p10+p01)
    rand = r.getrandbits(16)
    
    if (mean*65536) > rand:
        bit = 1
    else:
        bit = 0

    bits = [bit,]

    for i in range(bit_count-1):
        rand = r.getrandbits(16)
        if bit==0:
            #print("rand = %d, p = %d   " % (rand,p01*65536), end="")
            if (p01*65536) > rand:
                bit = 1
            else:
                bit = 0
        else:
            if (p10*65536) > rand:
                bit = 0
            else:
                bit = 1
            #print("bit %d   " % bit)
        bits.append(bit)
    return bits

def count(data):
    c1 = data[0]
    c11 = 0
    lastbit = c1
    for i,bit in enumerate(data[1:]):
        if lastbit == 1 and bit == 1:
            c11 += 1
        if bit == 1:
            c1 += 1
        lastbit = bit
    return c1,c11


