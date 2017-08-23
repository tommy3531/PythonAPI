from tweepy import API
from tweepy import OAuthHandler
from tweepy import Cursor
from Model.Social.Twitter.Twitter_Tweet_Model import Tweet
from pprint import pprint

import json

def get_twitter_auth():
    """ Setup Twitter Authentication.

        Return: tweepy.OAuth Obj
    """
    consumer_key = "xIoIkf3n510nQummRrToTcMEW"
    consumer_secret = "tTKglNhypBJerQSRJsE1hmhWzxZrolw85NRObjbjb38HLvbiAH"
    access_token = "852662587934130176-scJ8ZEtjtyWpiiqJfAEG5DnyVH6BleU"
    access_secret = "wxedTgkOhsX1DLymQ8wze6r2UYigtFOKiSehF9LU9bo98"

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    return auth

def get_twitter_client():
    """ Setup Twitter API Client.

        Return: tweepy.API object
    """
    auth = get_twitter_auth()
    client = API(auth)
    return client

def get_rep_information():
    client = get_twitter_client()
    user = "RepCleaver"
    data = Cursor(client.user_timeline, id=user).items(6)
    return data

def get_rep_tweet():
    repTweetList = []
    parseJson = get_rep_information()
    print("This is parse_rep_information: ")
    for items in parseJson:
        # print(json.dumps(items._json))
        tweet_ID = items._json['id_str']
        tweet_text = items._json['text']
        tweet_place = items._json['place']
        tweet_retweet = items._json['retweeted']
        tweet_retweetCount = items._json['retweet_count']
        tweet_screen_name_reply = items._json['in_reply_to_screen_name']
        tweet_status_id_reply = items._json['in_reply_to_status_id']
        tweet_status_id_str_reply = items._json['in_reply_to_status_id_str']
        tweet_user_id_reply = items._json['in_reply_to_user_id']

        repTweetObj = Tweet(tweet_ID, tweet_text, tweet_place, tweet_retweet, tweet_retweetCount, tweet_screen_name_reply, tweet_status_id_reply, tweet_status_id_str_reply, tweet_user_id_reply)
        repTweetList.append(repTweetObj)
    return repTweetList


def get_quoted_tweet():
    parseJson = get_rep_information()
    for num, items in enumerate(parseJson, start=1):
        if hasattr(items, 'quoted_status'):
            tweet_quote_id = items.quoted_status['id']
            #print(tweet_quote_id)
        else:
            tweet_quote_id = "None" + "\n"
        if hasattr(items, 'quoted_status'):
            tweet_quote_strID = items.quoted_status['id_str']
        else:
            tweet_quote_strID = "None" + "\n"

        if hasattr(items, 'quoted_status'):
            tweet_quote_text = items.quoted_status['text']
        else:
            tweet_quote_text = "None" + "\n"
        print("**********This is the quoted Tweet**********" + "TweetNum: " + str(num))
        print("This is the quoted TweetID: " + str(tweet_quote_id))
        print("This is the quoted TweetStrID: " + str(tweet_quote_strID))
        print("This is the quoted Tweet Text: " + str(tweet_quote_text))

def get_tweet_user_mention():
    parseJson = get_rep_information()
    for items in parseJson:
        for tag in (items.entities['user_mentions']):
            print("**********User Mentions**********" + "TweetNum: ")
            tweet_user_mention_screenName = tag['screen_name']
            tweet_user_mention_name = tag['name']
            tweet_user_mention_id = tag['id']
            tweet_user_mention_idStr = tag['id_str']
            print("This is the tweet User Mention tweet screen_name: " + str(tweet_user_mention_screenName))
            print("This is the tweet User Mention tweet name: " + str(tweet_user_mention_name))
            print("This is the tweet User Mention tweet id: " + str(tweet_user_mention_id))
            print("This is the tweet User Mention tweet strID: " + str(tweet_user_mention_idStr + "\n"))

def get_tweetQuote_hashtag():
    parseJson = get_rep_information()
    for num, items in enumerate(parseJson, start=1):

        # If the tweet was a quote get quoted tweet information
        # "quoted_status": { "entities": { "hashtags": [{ "text":}]
        if hasattr(items, 'quoted_status'):
            for element in items.quoted_status['entities']['hashtags']:
                if hasattr(element, 'text'):
                    hashtag = element['text']
                    print("**********This is the Tweet Quote HashTag**********" + "TweetNum: " + str(num) + "\n")
                    print("This is the quoted Tweet hashtag: " + str(hashtag) + "\n")
                else:
                    hashtag = "None"
                    print("**********This is the Tweet Quote HashTag**********" + "TweetNum: " + str(num) + "\n")
                    print("This is the quoted Tweet hashtag: " + str(hashtag) + "\n")
        else:
            hashtag = "None"
            print("**********This is the Tweet Quote HashTag**********" + "TweetNum: " + str(num))
            print("This is the quoted Tweet hashtag: " + str(hashtag) + "\n")

def tweet_quote_user_mention():
    parseJson = get_rep_information()
    for num, items in enumerate(parseJson, start=1):
        # Get the quoted tweet who mentioned users
        # ScreenName, name, id, tweetId
        if hasattr(items, 'quoted_status'):
            for item in items.quoted_status['entities']['user_mentions']:
                tweet_quote_user_mention_screenName = item['screen_name']
                tweet_quote_user_mention_name = item['name']
                tweet_quote_user_mention_id = item['id']
                tweet_quote_user_mention_id_str = item['id_str']
                print("**********This is the Tweet Quote UserMention**********" + "TweetNum: " + str(num))
                print("This is the quoted Tweet UserMention ScreenName: " + str(tweet_quote_user_mention_screenName))
                print("This is the quoted Tweet UserMention Name: " + str(tweet_quote_user_mention_name))
                print("This is the quoted Tweet UserMention id: " + str(tweet_quote_user_mention_id))
                print("This is the quoted Tweet UserMention idStr: " + str(tweet_quote_user_mention_id_str))
        else:
            tweet_quote_user_mention_screenName = "None"
            tweet_quote_user_mention_name = "None"
            tweet_quote_user_mention_id = "None"
            tweet_quote_user_mention_id_str = "None"
            print("**********This is the Tweet Quote UserMention**********" + "TweetNum: " + str(num))
            print("This is the quoted Tweet UserMention ScreenName: " + str(tweet_quote_user_mention_screenName))
            print("This is the quoted Tweet UserMention Name: " + str(tweet_quote_user_mention_name))
            print("This is the quoted Tweet UserMention id: " + str(tweet_quote_user_mention_id))
            print("This is the quoted Tweet UserMention idStr: " + str(tweet_quote_user_mention_id_str) + "\n")

if __name__ == '__main__':
    # tweet_quote_user_mention()
    #get_tweetQuote_hashtag()
    tweet_Model = get_rep_tweet()
    for i in tweet_Model:
        print(i.tweetID)

    # get_tweet_user_mention()
    # parse_rep_tweet()
    #parse_rep_information()

    # 'user_mentions': [{}]
    # 'source':
    # 'text':

    # Rep Twitter name
    # RepJasonSmith
    # USRepLong
    # RepSamGraves
    # RepCleaver

