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
        text = items._json['text']
        print("This is tweet:  " + str(text))
        for tag in items.entities['user_mentions']:
            print("This is the id: " + str(tag['id']))
            print("This is the screen_name: " + tag['screen_name'])
            print("This is the name: " + tag['name'] + "\n")

# def parse_rep_tweet():
#     parseJson = get_rep_information()
#     for items in parseJson:



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

