'''

 
 QUITO 
==============
'''
import couchdb
import sys
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
 
 

##########API CREDENTIALS ############   
#Colocar credenciales del API de dev de Twitter
ckey = "aS4zeGpMtFElhmHjo5j51B5Cq"
csecret = "372fqTyTB935wqLIHxxcXuO2ZYiE7zGJnRyXIc5t6WgJg6pN0U"
atoken = "337494712-W2ILwLCsDALdAYJjRsDgulmexO5HQnsBytsdjjY4"
asecret = "Vfatc38C95nR4lQMEg0XB6eBe1MK4JZEUnkLL0RIvNcxV"
 

 
class listener(StreamListener):
 
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
 
    def on_error(self, status):
        print (status)
 
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
 

URL = 'localhost'
db_name = 'rusia4'
 
'''========couchdb'=========='''
server = couchdb.Server('http://'+URL+':5984/')  #('http://245.106.43.184:5984/') poner la url de su base de datos
try:
    print (db_name)
    db = server[db_name]
 
except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()
 
 
'''===============LOCATIONS=============='''
 
twitterStream.filter(locations=[28.8382,59.367,30.7349,60.2335])
