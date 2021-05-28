from collections import Counter

import tweepy

auth = tweepy.OAuthHandler("eJsbJ33DET20aUDlmhIDgZZcw", "cyaOB1iG5HUWuLJ8tO85WSafd4IgCDL4U1uablTfjlunW1hqRR")
auth.set_access_token("1368674209350643712-c0EV5xPmQBS3LL3R87srZs1SVkHnny",
                      "KUCSb6mENVWEEORXIxLHSIJJaJGQfWunXH9Zd9Cw0thbh")

api = tweepy.API(auth)

query = "lessismore -filter:retweets"
max_tweets = 100
searched_tweets = [tweet.author.location for tweet in
                   tweepy.Cursor(api.search, q=query, lang="en", geocode="22.3511148,78.6677428,25000km").items(max_tweets)]

print(Counter(searched_tweets))

for key, value in sorted(Counter(searched_tweets).items(), key=lambda item: item[1], reverse=True):
    print(value, key)