import re, urllib, xml.etree.ElementTree as ET

token = "00bb6941952020d69e84be0ba5247468b97026b7"
service_url = "https://papapi.se/xml/?"
# z=201+23&token=

zipcode = "201 23"
zipcode = re.sub(r' +', "+", zipcode)

url = service_url+"z="+zipcode+"&token="+token


# get url data
print "retrieving", url
uh = urllib.urlopen( url )
data = uh.read()
print "retired", len(data), "characters"
#print data
tree = ET.fromstring( data )
#print tree
lst = tree.findall( "item/street" )

print "selected", len(lst)
