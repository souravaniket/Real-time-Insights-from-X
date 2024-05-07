import json
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

# Load WW_trends and US_trends data into the given variables respectively
WW_trends = json.loads(open(r'C:\Users\Aniket Sourav\Downloads\WWTrends.json').read())
US_trends = json.loads(open(r'C:\Users\Aniket Sourav\Downloads\USTrends.json').read())

# Pretty-printing the results. First WW and then US trends.
print("WW trends:", WW_trends)
print("\n", "US trends:", US_trends)

# Extracting all the WW trend names from WW_trends
world_trends = set([trend['name'] for trend in WW_trends[0]['trends']])
# Extracting all the US trend names from US_trends
us_trends = set([trend['name'] for trend in US_trends[0]['trends']])
# Getting the intersection of the two sets of trends
common_trends = world_trends.intersection(us_trends)
# Inspecting the data
print(world_trends, "\n")
print(us_trends, "\n")
print(len(common_trends), "common trends:", common_trends)

# Loading the data
tweets = json.loads(open(r"C:\Users\Aniket Sourav\Downloads\WWTrends.json").read())
# Inspecting some tweets
tweets[0:2]

# Extracting the text of all the tweets from the tweet object
texts = [tweet['text'] for tweet in tweets if 'text' in tweet]

# Extracting screen names of users tweeting about #WeLoveTheEarth
names = [user_mention['screen_name'] for tweet in tweets if 'entities' in tweet for user_mention in tweet['entities'].get('user_mentions', [])]

# Extracting all the hashtags being used when talking about this topic
hashtags = [hashtag['text'] for tweet in tweets if 'entities' in tweet for hashtag in tweet['entities'].get('hashtags', [])]

# Inspecting the first 10 results
print(json.dumps(texts[0:10], indent=1), "\n")
print(json.dumps(names[0:10], indent=1), "\n")
print(json.dumps(hashtags[0:10], indent=1), "\n")

# Counting occurrences/getting frequency dist of all names and hashtags
name_counter = Counter(names)
hashtag_counter = Counter(hashtags)

# Inspecting the 10 most common items in the counters
print(name_counter.most_common(10), "\n")
print(hashtag_counter.most_common(10), "\n")

retweets = [
    (tweet['retweet_count'],
     tweet['retweeted_status']['favorite_count'],
     tweet['retweeted_status']['user']['followers_count'],
     tweet['retweeted_status']['user']['screen_name'],
     tweet['text'])
    for tweet in tweets
    if 'retweeted_status' in tweet
]

# Create a DataFrame and visualize the data in a pretty and insightful format
df = pd.DataFrame(retweets, columns=['Retweets', 'Favorites', 'Followers', 'ScreenName', 'Text']).groupby(['ScreenName', 'Text', 'Followers']).sum().sort_values(by=['Followers'], ascending=False)

df.style.background_gradient()

# Extracting language for each tweet and appending it to the list of languages
tweets_languages = [tweet['lang'] for tweet in tweets if 'lang' in tweet]

# Extracting source for each tweet and appending it to the list of sources
tweets_sources = [tweet['source'] for tweet in tweets if 'source' in tweet]

# Plotting the distribution of languages
plt.hist(tweets_languages)
plt.hist(tweets_sources)
plt.show()
