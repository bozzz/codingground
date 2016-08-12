# -*- coding: latin-1 -*-
import codecs

def conversion(old):
    direction = {'N':1, 'S':-1, 'E': 1, 'W':-1}
    new = old.replace(u'°',' ').replace('\'',' ').replace('"',' ')
    new = new.split()
    try:
        x = int(new[0])
        new_dir = new.pop()
    except:
        new_dir = new.pop(0)
   
    new.extend([0,0,0])
    return (float(new[0])+float(new[1])/60.0+float(new[2])/3600.0) * direction[new_dir]

#lat, lon = u'''0°25'30"S, 91°7'W'''.split(', ')
#lat, lon = u'''N 60° 26.457', E 15° 29.518'''.split(', ')

#print conversion(lat), conversion(lon)

#f = open( 'loomis.txt', "r" )
f = codecs.open('loomis.txt', encoding='latin-1')
for aline in f.readlines( ):
    #aline = aline.encode('latin-1')
    values = aline.split( " : " )
    coord = values[ 1 ].split( ', ' ) 
    print values[ 0 ], conversion( coord[ 0 ] ), conversion( coord[ 1 ] )
    
## close the file after reading the lines.
f.close()
