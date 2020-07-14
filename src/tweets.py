# coding: utf-8
import GetOldTweets3 as got
import pandas as pd 

def getTweets(username, maxTweets):
  tweetCriteria = got.manager.TweetCriteria().setUsername(username)\
                                           .setTopTweets(True)\
                                           .setMaxTweets(maxTweets)
  tweets = got.manager.TweetManager.getTweets(tweetCriteria)
  return tweets

def buildDataFrame(tweets):
  tweet_text=[]
  tweet_username=[]
  tweet_id=[]
  tweet_date=[]
  tweet_hashtags=[]
  for tweet in tweets:
    tweet_text.append(tweet.text)
    tweet_username.append(tweet.username)
    tweet_id.append(tweet.id)
    tweet_date.append(str(tweet.date).split(" ")[0])
    tweet_hashtags.append(tweet.hashtags)
  return pd.DataFrame({"tweets": tweet_text, "ids": tweet_id, "username": tweet_username, "date": tweet_date, "hashtags": tweet_hashtags})


def main():
    username = "fogocruzadoapp"
    maxTweets = 10
    getTweets(username, maxTweets)

if __name__ == '__main__':
    main()
