from __future__ import unicode_literals
import tweepy,sys
#get your consumer key and access key from https://dev.twitter.com/
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

#file input as command to write them in the file
fil=sys.argv[1]
data ={}
class MyStreamListener(tweepy.StreamListener):
    i=1
    def on_status(self, status):
        try:    
            oFile = open(fil,"a")
            data['name'] = status.user.name
            #data['screen_name'] = status.user.screen_name optional
            data['location'] = status.user.location
            data['text'] = status.text
            data['created_at'] = status.created_at 
            #data['geo'] = status.coordinates optional
            #data['source'] = status.source 
            #print(status.text)
            s=str(MyStreamListener.i)
            data_location = str(data['location'])
            data_text = str(data['text']).encode('utf-16', 'ignore').decode('utf-16','ignore')
            data_time = str(data['created_at'])
            if "Hurricane" in data_text and "Irma" in data_text and "RT" not in data_text:
                print(data_text)
                oFile.write(data_text+">>>>"+data_location+">>>>"+data_time+">>>>"+s+"\n")
                MyStreamListener.i +=1
        except:
            pass
        def on_timeout(self):
            print >> sys.stderr, 'Timeout...'
            return True # Don't kill the stream
            print "Stream restarted"

myStreamListener = MyStreamListener()
def start_stream():
    while True:
        try:
            myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
            myStream.filter(track=['Hurricane' and 'Irma'])
        except: 
            continue
start_stream()
oFile = open(fil)
oFile.close()

