#!/usr/bin/env python3

from __future__ import print_function
from __future__ import division

import math
import random
import sys

import markov2p as m
import generate as g
import polygon as p

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
        p01,p10 = m.pick_point(entropy,0.0000001,16,quiet=True)
        print("p01,p10 = %f,%f = 0x%04X,0x%04X, " % (p01,p10,int(p01*65535), int(p10*65535)),end="")

        pass_count = 0
        fail_count = 0
        total_count = 0

        for i in range(256):
            data = g.generate(p01,p10,2304)
            bias,scc = m.p_2_biasscc(p01,p10)

            c1,c11 = g.count(data)
            if i==0:
                if scc < 0.0:
                    print("c1,c11=%04d,%04d mu,scc=%0.3f,%0.3f " % (c1,c11,bias,scc), end="")
                else:
                    print("c1,c11=%04d,%04d mu,scc=%0.3f, %0.3f " % (c1,c11,bias,scc), end="")
            if p.inside_polygon(c1,c11):
                pass_count += 1
                total_count += 1
            else:
                fail_count += 1
                total_count += 1
        print("HR = %f" % (float(pass_count) / total_count))

    
