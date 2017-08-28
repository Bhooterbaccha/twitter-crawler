from __future__ import unicode_literals
import tweepy,sys
#get your consumer key and access key from https://dev.twitter.com/
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

#file input as command to write them in the file
fil=sys.argv[1]

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
    	try:
    		oFile = open(fil,"a")
    	#if 'flood' in status.text:
    		print(status.text.encode('utf-8', 'ignore').decode('utf-8','ignore'))
        
        	oFile.write(status.text.encode('utf-8', 'ignore').decode('utf-8','ignore')+"\n")
        except:
        	pass	
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['flood' and 'gujarat']) #any search term to filter tweets as per the need.
