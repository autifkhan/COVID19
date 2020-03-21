#!/usr/bin/python

def load( f = 'confirmed' ):
    lines = open( f ).readlines()
    res = []
    for l in lines:
        qs = l.split( '"' )
        nqs = len( qs )
        if( 1 == nqs ):
            res.append( l.strip().split(',') );
            #print( l.strip() )
        elif( 3 == nqs ):
            res.append( (qs[0] + qs[1].replace( ',', '' ) + qs[2]).strip().split(',') )
            #print( (qs[0] + qs[1].replace( ',', '' ) + qs[2]).strip() )
        else:
            print( "========== FAILED =========" )
            print( l.strip() )
            print( "========== FAILED =========" )
    return res

def name( l ):
    if( '' == l[0] ):
        return l[1]
    else:
        return l[1] + ' - ' + l[0]

def vs_data( f_, d ):
    f = open( f_, "w" )
    n = 0
    for i_ in d:
        try:
            i = int( i_)
            if i and int(i) > 100:
                n = n + 1
                f.write( "%d %d\n" % (n,i) )
        except:
            pass
    f.close()

def growth( f_, d ):
    f = open( f_, "w" )
    n = 0
    started = False
    for i in range( 5, len( d ) ):
        if( int(d[i]) > 100 ):
            started = True
        else:
            continue
        if( not started ):
            continue

        n = n+1
        g = int(d[i]) - int(d[i-1])
        f.write( "%d %d\n" % (n, g) )
    f.close()
