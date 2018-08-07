__author__ = 'diegoguaman'

'''


 QUITO
==============
'''
import couchdb
import sys
import urllib2
import re
import json

regex = re.compile(r'[A-z a-z 0-9]+')

from couchdb import view

URL = 'localhost'
db_name = 'croacia'


'''========couchdb'=========='''
server = couchdb.Server('http://localhost:5984/')  #('http://245.106.43.184:5984/') poner la url de su base de datos
try:
    print (db_name)
    db = server[db_name]
    print ('success')

except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()



url = 'http://127.0.0.1:5984/croacia/_design/croacia15JulCoordenadasOp/_view/croacia15JulCoordenadasOp'
req = urllib2.Request(url)
f = urllib2.urlopen(req)
d = json.loads(f.read())
data = {}
data ['people'] = []
for x in d['rows']:
	a = x ['value']

	data ['people'].append({'text': x })
	with open ('CoordenadasCroaciaFinal.txt' , 'w') as outfile:
		json.dump(data,outfile)
		print (data)
f.close()