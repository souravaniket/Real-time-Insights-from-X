import json
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

# Load WW_trends and US_trends data into the given variables respectively
WW_trends = json.loads(open(r'C:\Users\Aniket Sourav\Downloads\WWTrends.json').read())
US_trends = json.loads(open(r'C:\Users\Aniket Sourav\Downloads\USTrends.json').read())

# Extracting all the WW trend names from WW_trends
world_trends = set([trend['name'] for trend in WW_trends[0]['trends']])
# Extracting all the US trend names from US_trends
us_trends = set([trend['name'] for trend in US_trends[0]['trends']])
# Getting the intersection of the two sets of trends
common_trends = world_trends.intersection(us_trends)
# Inspecting the data
print("Common trends:", common_trends)

# Loading the data
tweets = json.loads(open(r"C:\Users\Aniket Sourav\Downloads\WWTrends.json").read())

# Extracting the text of all the tweets from the tweet object
texts = [tweet['text'] for tweet in tweets if 'text' in tweet]

# Extracting screen names of users tweeting about #WeLoveTheEarth
names = [user_mention['screen_name'] for tweet in tweets if 'entities' in tweet for user_mention in tweet['entities'].get('user_mentions', [])]

# Extracting all the hashtags being used when talking about this topic
hashtags = [hashtag['text'] for tweet in tweets if 'entities' in tweet for hashtag in tweet['entities'].get('hashtags', [])]

# Inspecting the first 10 results
print("Texts:", json.dumps(texts[0:10], indent=1))
print("Names:", json.dumps(names[0:10], indent=1))
print("Hashtags:", json.dumps(hashtags[0:10], indent=1))

# Counting occurrences/ getting frequency dist of all names and hashtags
for item in [names, hashtags]:
    c = Counter(item)
    # Inspecting the 10 most common items in c
    print("Most common items:", c.most_common(10))

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

# Extracting language for each tweet and appending it to the list of languages
tweets_languages = [tweet['lang'] for tweet in tweets if 'lang' in tweet]

# Extracting sources for each tweet and appending it to the list of sources
tweets_sources = [tweet['source'] for tweet in tweets if 'source' in tweet]

# Plotting the distribution of languages
plt.hist(tweets_languages)
plt.title('Distribution of Languages')
plt.xlabel('Languages')
plt.ylabel('Frequency')
plt.show()

# Plotting the distribution of tweet sources
plt.hist(tweets_sources)
plt.title('Distribution of Tweet Sources')
plt.xlabel('Tweet Sources')
plt.ylabel('Frequency')
plt.show()
