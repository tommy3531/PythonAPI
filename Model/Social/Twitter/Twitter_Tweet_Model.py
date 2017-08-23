class Tweet():

    def __init__(self, tweet_ID, tweet_text, tweet_place, tweet_retweet, tweet_retweetCount, tweet_screen_name_reply, tweet_status_id_reply, tweet_status_id_str_reply, tweet_user_id_reply):
        self.tweetID = tweet_ID
        self.tweetText = tweet_text
        self.tweetPlace = tweet_place
        self.tweetRetweet = tweet_retweet
        self.tweetRetweetCount = tweet_retweetCount
        self.tweetScreenNameReply = tweet_screen_name_reply
        self.tweetStatusIDReply = tweet_status_id_reply
        self.tweetStatusIDStrReply = tweet_status_id_str_reply
        self.tweetUserIDReply = tweet_user_id_reply