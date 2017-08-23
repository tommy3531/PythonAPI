class Tweet:

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

# Need to add getter to retreived individual object attributes

class Tweet_UserMention():

    def __init__(self, tweet_user_mention_screenName, tweet_user_mention_name, tweet_user_mention_id, tweet_user_mention_idStr):

        self.tweetUserMentionScreenName = tweet_user_mention_screenName
        self.tweetUserMentionName = tweet_user_mention_name
        self.tweetUserMentionID = tweet_user_mention_id
        self.tweetUserMentionIDStr = tweet_user_mention_idStr

class Tweet_Quoted():

    def __init__(self, tweet_quote_id, tweet_quote_strID, tweet_quote_text):
        self.tweetQuotedID = tweet_quote_id
        self.tweetQuotedStrID = tweet_quote_strID
        self.tweetQuotedText = tweet_quote_text

class Tweet_Quoted_HashTag():

    def __init__(self, tweet_quote_hashTag):
        self.tweetQuoteHashTag = tweet_quote_hashTag

class Tweet_Quoted_UserMention():

    def __init__(self, tweet_quote_user_mention_screenName, tweet_quote_user_mention_name, tweet_quote_user_mention_id, tweet_quote_user_mention_id_str):
        self.tweetQuoteUserMentionScreenName = tweet_quote_user_mention_screenName
        self.tweetQuoteUserMentionName = tweet_quote_user_mention_name
        self.tweetQuoteUserMentionID = tweet_quote_user_mention_id
        self.tweetQuoteUserMentionIDStr = tweet_quote_user_mention_id_str