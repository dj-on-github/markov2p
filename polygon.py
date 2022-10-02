import math
import sys

# Multiplies done with shifts, adds and subtracts
# 
# Multiplying by 2 involves shifting left, but if it's negative
# you must only shift the positive bits and hold the negative msb where it is.
# If it's positive, just shift right.


def s17_mult_by_2(x):
    mask = 0x01FFFF
    msb  = 0x010000
    
    if ((x & msb) == 0):
        return (x << 1)   # positive so shift
    return (((x << 1) | 0x010000) & mask) # Negative, so keep the msb==1


def s17_mult_by_5(x):
    mask = 0x01FFFF
    msb  = 0x010000
    
    # positive
    if ((x & msb) == 0):
        return s17_add(x,(x << 2))  # x*4 + x = x*5
    
    # negative
    return s17_add(x,(((x << 1) | 0x10000) & mask))


def s17_mult_by_10(x):
    mask = 0x01FFFF
    msb  = 0x010000
    
    # positive
    if ((x & msb) == 0):
        return s17_add((x << 1),(x << 3)) # x*8 + x*2 = x*10;
    
    # negative
    return s17_add( (((x << 3) | 0x10000) & mask),(((x << 1) | 0x10000) & mask))


def s17_mult_by_15(x):
    mask = 0x01FFFF
    msb  = 0x010000
    
    # positive
    if ((x & msb) == 0):
        return s17_sub((x << 4),x) # x*16 - x = x*15;
    
    # negative
    return s17_sub( (((x << 4) | 0x10000) & mask), x )


def s17_mult_by_20(x):
    mask = 0x01FFFF;
    msb = 0x010000;
    
    # positive
    if ((x & msb) == 0):
        return s17_add((x << 4),(x << 2)) # x*16 + x*4 = x*20;
    
    # negative
    return s17_add( (((x << 4) | 0x10000) & mask), (((x << 2) | 0x10000) & mask) )

def s17_add(x, y):
    mask = 0x01FFFF
    
    return ((x+y) & mask)

def s17_sub(x, y):
    mask = 0x01FFFF

    return ((x-y) & mask)


def s17_x_lt_y(x,y):
    msb = 0x010000
    if ((s17_sub(x,y) & msb) == msb):
        return True
    return False


def s17_x_gt_y(x,y):
    msb = 0x010000
    if ((s17_sub(x,y) & msb) == 0):
        return True
    return False

def inside_polygon(c1, c11):
    five_c11 = s17_mult_by_5(c11)
    five_c1 =  s17_mult_by_5(c1)
    
    fifteen_c11 = s17_mult_by_15(c11)
    #printf("c11 = %d, fifteen_c11 = %d\n", c11, fifteen_c11);
    
    ten_c11 = s17_mult_by_10(c11)
    #printf("c11 = %d, ten_c11 = %d\n", c11, ten_c11);
    
    two_c1 = s17_mult_by_2(c1)
    #printf("c1 = %d, two_c1 = %d\n", c1, two_c1);
    
    ten_c1 = s17_mult_by_10(c1)
    #printf("c1 = %d, ten_c1 = %d\n", c1, ten_c1);
    
    twenty_c1 = s17_mult_by_20(c1)
    #printf("c1 = %d, twenty_c1 = %d\n", c1, twenty_c1);
    
    ab_ok = s17_x_lt_y(fifteen_c11, (s17_sub(twenty_c1,4*2303)))
    #printf("s17_sub(twenty_c1,4*2303) = %d\n", s17_sub(twenty_c1,4*2303));

    bc_ok = s17_x_lt_y(fifteen_c11, (s17_add(ten_c1,2303)))
    #printf("s17_add(ten_c1,2303) = %d\n", s17_add(ten_c1,2303))
    
    dc_ok = s17_x_gt_y(c11,(s17_sub(two_c1,2303)))
    #printf("c11=%d > s17_sub(two_c1,2303) = %d\n", c11, s17_sub(two_c1,2303));
    
    ed_ok = s17_x_gt_y(five_c11,(s17_sub(five_c1,2*2303)))
    #printf("s17_sub(ten_c1,2*2303) = %d\n", s17_sub(ten_c1,2*2303));
    
    if (ab_ok and bc_ok and dc_ok and ed_ok):
        return True
    else:
        return False;
    

def mean_scc_to_p1_p11(mean, scc):
    
    p10 = (1.0-mean)*(1.0-scc)
    p01 = mean*(1.0-scc)
    p11 = 1.0-p10
    p1 = mean

    return p1, p11

# Sign extend to int for display of negatives
def s17_sex(x):
    msb = 0x010000
    if ((x & msb)==msb):
        n = x & 0x00ffff
        n = n - 0x010000
        return n
    else:
        return x  

