#!/usr/bin/env python3.9

from __future__ import print_function
from __future__ import division

import math
import random
import sys

import markov2p as m

def usage():
    print("Usage: mk_mkv_points <entropy rate> <# points>") 

if __name__ == '__main__':
    if len(sys.argv) != 3:
        usage()
        exit(0)

    if sys.argv[1] in ["-h", "help", "--help"]:
        usage()
        exit(0)

    entropy = float(sys.argv[1])
    num_of_points = int(sys.argv[2])

    for i in range(num_of_points):
        p01,p10 = m.pick_point(entropy,0.0000001,10,quiet=True)
        print("p01,p10 = %f,%f = 0x%04X,0x%04X" % (p01,p10,int(p01*65535), int(p10*65535)))

    
