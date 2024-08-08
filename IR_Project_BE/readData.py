import snscrape.modules.twitter as sntwitter
import pandas as pd


def generateData():
    query = "earthquake (help OR stuck) (#earthquake)"
    tweets =[]
    limit = 500
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if len(tweets) == limit:
            break
        else:
            tweets.append([tweet.date,tweet.user.username,tweet.rawContent, tweet.user.location])
    df= pd.DataFrame(tweets,columns=['Date','User','Tweet','Location'])
    print(df)
    return df