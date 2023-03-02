import json
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import re
from PIL import Image
import numpy as np


def tweet_filter(word):

    if word.startswith('#') or word.startswith('http'):
        return False
    elif word in banned_words:
        return False
    else:
        return True

# load the json file
with open('data/crypto_june2022.json', 'r') as f:
    data = json.load(f)

# wordcloud wants a signel text, then it is necessary
# to concatenate all the content in a signel text
# excluding the word 'nuclear' and 'energy' and 'https'

# banned_words = ['energy', 'nuclear', 'nuclearenergy', 'uranium', 'reactor'] FOR NUCLEAR
banned_words = ['amp', 'sex', 'will', 'next', 'new', 'X', 'market', 'weekend', 'time', 'crypto', 'rt'] # FOR CRYPTO

text = ''

stopwords = set(STOPWORDS)

for tweet in data:

    tweet = tweet['content'].lower()
    # apply the filter
    tweet = " ".join(list(filter(tweet_filter, tweet.split(' '))))
    # further filter for http
    tweet = re.sub(r'http\S+', '', tweet)
    # filter for non english characters
    tweet = "".join(list(filter(lambda ele: re.search("[a-zA-Z\s]+", ele) is not None, tweet)))
    text += tweet

# set the shape
cloud_mask = np.array(Image.open('cloud.png'))

wordcloud = WordCloud(background_color="white", stopwords=stopwords, mask=cloud_mask)
wordcloud.generate(text)

# display the wordcount
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

wordcloud.to_file('images/crypto_june2022.png')