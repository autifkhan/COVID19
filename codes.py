#!/usr/bin/python

from util import load, name

def codes( d, n ):
    f = open( str(n) + ".txt", "w" )
    for i in range( 1, len( d ) ):
        for j in range( 4, len( d[i] ) ):
            if( int( d[i][j] ) > n ):
                f.write( "%d - %s\n" % (i+1, name( d[i] ) ) )
                break
    f.close()

d = load()
codes( d, 0 )
codes( d, 100 )
codes( d, 500 )
codes( d, 1000 )

