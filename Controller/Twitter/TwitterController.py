from tweepy import API
from tweepy import OAuthHandler
from tweepy import Cursor
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
    data = Cursor(client.user_timeline, id=user).items(1)
    return data

def parse_rep_entity():
    parseJson = get_rep_information()
    print("This is parse_rep_information: ")
    for items in parseJson:
        # print(json.dumps(items._json))

        tweetID = items._json['id_str']
        text = items._json['text']
        place = items._json['place']
        retweet = items._json['retweeted']
        retweetCount = items._json['retweet_count']
        screen_name_reply = items._json['in_reply_to_screen_name']
        status_id_reply = items._json['in_reply_to_status_id']
        status_id_str_reply = items._json['in_reply_to_status_id_str']
        user_id_reply = items._json['in_reply_to_user_id']
        if items.quoted_status:
            tweet_quote_id = "None"
        else:
            tweet_quote_id = items.quoted_status['id']
        tweet_quote_strID = items.quoted_status['id_str']
        tweet_quote_text = items.quoted_status['text']
        print("Tweet Information")
        print("This is the tweet ID: " + str(tweetID))
        print("This is the tweet text:  " + str(text))
        print("This is the tweet place: " + str(place))
        print("This is the tweet retweeted: " + str(retweet))
        print("This is the tweet reply Screen Name: " + str(screen_name_reply))
        print("This is the tweet reply ID: " + str(status_id_reply))
        print("This is the tweet reply status ID: " + str(status_id_str_reply))
        print("This is the tweet reply user ID: " + str(user_id_reply))
        print("This is the tweet retweet count: " + str(retweetCount) + "\n")

        print("This is the quoted Tweet")
        print("This is the quoted TweetID: " + str(tweet_quote_id))
        print("This is the quoted TweetStrID: " + str(tweet_quote_strID))
        print("This is the quoted Tweet Text: " + str(tweet_quote_text + "\n"))

        for tag in items.entities['user_mentions']:
            print("User Mentions")
            tweet_user_mention_screenName = tag['screen_name']
            tweet_user_mention_name = tag['name']
            tweet_user_mention_id = tag['id']
            tweet_user_mention_idStr = tag['id_str']
            print("This is the tweet User Mention tweet screen_name: " + str(tweet_user_mention_screenName))
            print("This is the tweet User Mention tweet name: " + str(tweet_user_mention_name))
            print("This is the tweet User Mention tweet id: " + str(tweet_user_mention_id))
            print("This is the tweet User Mention tweet strID: " + str(tweet_user_mention_idStr + "\n"))

        # If the tweet was a quote get quoted tweet information
        # "quoted_status": { "entities": { "hashtags": [{ "text":}]
        for element in items.quoted_status['entities']['hashtags']:
            hashtag = element['text']
            print("This is the quoted Tweet hashtag: " + str(hashtag))

        # Get the quoted tweet who mentioned users
        # ScreenName, name, id, tweetId
        for item in items.quoted_status['entities']['user_mentions']:
            tweet_quote_user_mention_screenName = item['screen_name']
            tweet_quote_user_mention_name = item['name']
            tweet_quote_user_mention_id = item['id']
            tweet_quote_user_mention_id_str = item['id_str']
            print("This is the quoted Tweet UserMention ScreenName: " + str(tweet_quote_user_mention_screenName))
            print("This is the quoted Tweet UserMention Name: " + str(tweet_quote_user_mention_name))
            print("This is the quoted Tweet UserMention id: " + str(tweet_quote_user_mention_id))
            print("This is the quoted Tweet UserMention idStr: " + str(tweet_quote_user_mention_id_str))



if __name__ == '__main__':

    parse_rep_entity()
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

