import snscrape.modules.twitter as sntwitter
import json
import logging

# Set up logging to write messages to a file named 'scraping.log'
logging.basicConfig(filename='scraping.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Prompt the user to enter a search query for Twitter tweets
while True:
    query = input('Enter a search query for Twitter tweets: ')
    if len(query) == 0:
        print('Please enter a non-empty search query.')
    else:
        break

# Prompt the user to enter a maximum number of tweets to scrape
while True:
    try:
        limits = int(input('Enter the maximum number of tweets to scrape: '))
        if limits <= 0:
            raise ValueError
        break
    except ValueError:
        print('Please enter a positive integer value for the maximum number of tweets.')

# Initialize an empty list to store the scraped tweets
tweets = []

# Initialize a counter for assigning unique IDs to each tweet
id_counter = 0 

# Loop through the TwitterSearchScraper object to scrape tweets that match the search query
for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    # Break out of the loop if the maximum number of tweets has been reached
    if len(tweets) == limits:
        break
    else:
        # Create a dictionary to store information about the tweet
        t_dict = {}

        # Assign a unique ID to the tweet
        t_dict['_id'] = id_counter

        # Store the tweet date as a string
        t_dict['date'] = str(tweet.date)

        # Store the number of likes, content, replies, retweets, and quotes for the tweet
        t_dict['likes'] = tweet.likeCount
        t_dict['content'] = tweet.content
        t_dict['replies'] = tweet.replyCount
        t_dict['retweets'] = tweet.retweetCount
        t_dict['quotes'] = tweet.quoteCount

        # Append the tweet dictionary to the list of tweets and increment the ID counter
        tweets.append(t_dict)
        id_counter += 1

# Prompt the user to enter a filename to save the scraped tweets as a JSON file
while True:
    filename = input('Enter a filename to save the scraped tweets as a JSON file: ')
    if len(filename) == 0:
        print('Please enter a non-empty filename.')
    elif not filename.endswith('.json'):
        print('Please enter a filename with a .json extension.')
    else:
        break

# Save the scraped tweets as a JSON file
with open(filename, 'w') as f:
    json.dump(tweets, f, indent=4)

# Log a message to indicate that the process is complete
logging.info('Scraping process complete. Scraped {} tweets and saved to {}.'.format(len(tweets), filename))
