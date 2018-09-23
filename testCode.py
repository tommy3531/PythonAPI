from Bills import billDetails, getBillDetails
import Members as member
from News_Controller import listArticleFromSource, listSourceByCategory, listSources
from TwitterController import get_twitter_client, get_rep_information, get_rep_tweet, get_tweet_user_mention, get_tweetQuote_hashtag, tweet_quote_user_mention


# house = member.houseRepsByStateJSON("MO")
# senate = member.sentatorByStateJSON("MO")
# arrayHouse = member.parseHouse(house)
# arrySenator = member.parseSenator(senate)
# member.printHouse(arrayHouse)
# member.printSenator(arrySenator)
#
# sources = listSources()
# print(sources)

# tweet_Model = get_rep_tweet()
# for i in tweet_Model:
#     print(i.tweetID)

# tweet_user_mention = get_tweet_user_mention()
# for i in tweet_user_mention:
#     print(i.tweetUserMentionScreenName)

# tweet_Quote_HashTag = get_tweetQuote_hashtag()
# for i in tweet_Quote_HashTag:
#     print(i.tweetQuoteHashTag)

tweet_Quote_UserMention = tweet_quote_user_mention()
for i in tweet_Quote_UserMention:
    print(i.tweetQuoteUserMentionScreenName)
