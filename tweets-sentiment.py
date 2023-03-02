from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import json
import numpy as np
import pandas as pd
import os

# TODO use stemming

# preprocessing
def preprocess(tweet):

    tweet = tweet.lower()

    t_words = []

    for word in tweet.split(' '):
        if word.startswith('@') and len(word) > 1:
            word = '@user'

        elif word.startswith('http'):
            word = 'http'

        t_words.append(word)

    tweet = " ".join(t_words)
    return tweet

def do_sentiment(tweet, tokenizer, model, labels, return_prob=False):

    encoded_tweet = tokenizer(tweet, return_tensors='pt')
    output = model(**encoded_tweet)

    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    if return_prob:
        return labels[np.argmax(scores)], np.max(scores)
    else:
        return labels[np.argmax(scores)]

def get_sentiment_coefficient(sentiment_dict):
    # value in [0, 100]
    tot_tweets = 0
    numerator = 0.0
    for k, v in sentiment_dict.items():
        tot_tweets += v
        if k == 'neutral':
            numerator += v * 50.0
        elif k == 'positive':
            numerator += v * 100.0

    return numerator / tot_tweets

# load the model
roberta = 'cardiffnlp/twitter-roberta-base-sentiment'
model = AutoModelForSequenceClassification.from_pretrained(roberta)

tokenizer = AutoTokenizer.from_pretrained(roberta)

labels = ['negative', 'neutral', 'positive']

data_dir = 'data'
data_files = list(filter(lambda name: 'crypto' in name, os.listdir(data_dir)))

global_dict = {}

for _file in data_files:

    # get the month
    month = _file.split('_')[1].split('.')[0]

    # load the json file
    with open(os.path.join(data_dir, _file), 'r') as f:
        data = json.load(f)

    # inizialize a dictionary to keep track of the results
    sentiment_dict = {x:0 for x in labels}

    for tweet in data :

        tweet = tweet['content']
        tweet = preprocess(tweet)
        # sentiment analysis
        result = do_sentiment(tweet, tokenizer, model, labels)
        # update result
        sentiment_dict[result] += 1

    sentiment_coef = get_sentiment_coefficient(sentiment_dict)
    global_dict[month] = sentiment_coef

    print(f'Sentiment Coefficient: {sentiment_coef:.2f} % for {month}')


# save the global dict
with open(os.path.join(data_dir, 'crypto_year22.json'), 'w') as f:
    json.dump(global_dict, f, indent=4)

