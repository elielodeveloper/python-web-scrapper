# coding: utf-8
import GetOldTweets3 as got 

def getTweets(username, maxTweets):
  tweetCriteria = got.manager.TweetCriteria().setUsername(username)\
                                           .setTopTweets(True)\
                                           .setMaxTweets(maxTweets)
  tweets = got.manager.TweetManager.getTweets(tweetCriteria)
  for tweet in tweets:
    print(tweet.text)
  

def main():
    username = "fogocruzadoapp"
    maxTweets = 10
    getTweets(username, maxTweets)

if __name__ == '__main__':
    main()
