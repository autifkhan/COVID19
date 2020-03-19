#!/usr/bin/python

import sys

with open( 'confirmed' ) as f:
    a = f.readlines()

d = a[int(sys.argv[1]) - 1].split(',')
n = 0
for i_ in d:
    try:
        i = int(i_)
        if i and int(i) > 100:
            n = n + 1
            print "%d, %d" % (n, i)
    except:
        pass
