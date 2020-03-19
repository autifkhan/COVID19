#!/usr/bin/python

import sys

with open( 'confirmed' ) as f:
    a = f.readlines()

d = a[int(sys.argv[1]) - 1].split(',')
if d[0]:
    print "%s - %s" % (d[1], d[0])
else:
    print d[1]
