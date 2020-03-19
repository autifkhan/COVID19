#!/usr/bin/python

import sys

with open( 'confirmed' ) as f:
    a = f.readlines()

for i in range( 1, len( a ) ):
    d = a[i].split(',')
    if d[0]:
        print "%d : %s - %s" % ( i+1, d[1], d[0] )
    else:
        print "%d : %s" % ( i+1, d[1] )
