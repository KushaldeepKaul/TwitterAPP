import tweepy
from time import sleep
ckey='IHLgSQZnNWPuV69gadlEhUIhs'
csecret='jjvsLcPAfLQ8LZ8FMXTIZbwlrM1ZICjey88GMYuXm5hradp1II'
atoken='1011299384066232320-jnp3RS8BZakfEwEJUSVXSPCjM0MmbI'
asecret='q9BYcOvFCqDN6kfjklKyFcVSdz2IoI51m4Vv7Fe1FFFfK'


auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)
client = tweepy.API(auth)
print('Connected as @{}, you can start to tweet !'.format(client.me().screen_name))
client_id = client.me().id

def tweetAMessage():
    message=input("Please Enter Message=")
    print(message)
    try: 
        api.update_status(message)
        print("Your Message is Updated")
    except Exception as e:
        print("Duplicate Tweet")
def retrieveLastTweet():
    try:
        print("Your Last Updated Tweet Is")
        tweet = client.user_timeline(id =client_id, count = 1)[0]
        print(tweet.text)
    except Exception as e:
        print("ERROR!")

def retrieveAll():
    no=int(input("Please Enter no of tweet you want to retrieve="))
    try:
        tweet = client.user_timeline(id =client_id,count=no)
        v=0
        for t in tweet:
            print(tweet[v].text)
            v=v+1
    except Exception as e:
        print("You value more than no of tweets Please try again")
def homeline():
    try:
        tweets = api.home_timeline()
        v=0
        for tweet in tweets:
            print(tweet.text)
            v=v+1
    except Exception as e:
        print("ERROR!")
def retweet():
    try:
        subject=input("Please Enter Your Subject ")
        for tweet in tweepy.Cursor(api.search,q=subject).items(10):
            print('\nTweet by: @' + tweet.user.screen_name)
    except Exception as e:
        print("ERROR")

def countFolloowers():
     try:
        followers = tweepy.Cursor(api.followers, id = client_id)
        temp = []
        for user in followers.items():
            temp.append(user)
            
        if len(temp)<=0:
            print("Total No Of Followers ",len(temp))
        else:
            print("Total No Of Followers ",len(temp))
            print(temp)
     except Exception as e:
        print("ERROR!")
def getAllFollowers():
    try:
        followers = tweepy.Cursor(api.followers, id = client_id)
        temp = []
        for user in followers.items():
            temp.append(user)
            
        if len(temp)<=0:
            print("No Followers")
        else:
            print(temp)
    except Exception as e:
        print("ERROR!")
def countPersonFollower():
    hashTag=input("Please Enter Name Of Person You Want To check followers ")
    targets=[]
    targets.append(hashTag)
    for target in targets:
        user = api.get_user(target)
        print(user.name, user.followers_count)
def exitMethod():
    exit()
#For Updating the status
print("Menu")
print("1.\tCheck Followers Of Specific Person ")
print("2.\tCount the followers")
print("3.\tRetrieve All Your Tweets")
print("4.\tRetrieve HomeLine")
print("5.\tCompare tweets")
print("6.\tRetrieve Last Tweet")
print("7.\tTweet a message")
print("8.\tSearch Name of Person Who Tweet On Specific Subject ")
print("9.\tGet Name Of All Followers ")
print("10.\tExit")
while(True):
    value=int(input("What do you wanna do? "))

    if value==1:
        countPersonFollower()
    elif value==2:
        countFolloowers()
    elif value==3:
        retrieveAll()
    elif value==4:
        homeline()
    elif value==5:
        retrieveAll()
    elif value==6:
        retrieveLastTweet()  
    elif value==7 :
        tweetAMessage()
    elif value==8:
        retweet()
    elif value==9:
        getAllFollowers()
    elif value==10:
        exitMethod()

            # Retweet tweets as they are found
    '''tweet.retweet()
        print('Retweeted the tweet')
    '''




              
              
