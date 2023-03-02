# Twitter Scraping Script
This is a Python script that uses the `snscrape` library to scrape tweets from Twitter based on a user-specified search query, and save the scraped tweets as a JSON file. The script prompts the user to enter a search query for Twitter tweets, a maximum number of tweets to scrape, and a filename to save the scraped tweets as a JSON file. It also performs input validation to ensure that the user inputs are valid.

## Dependencies
This script requires the following Python libraries to be installed:

- `snscrape` (for scraping Twitter tweets)
- `pandas` (for data analysis)
- `json` (for working with JSON data)

These libraries can be installed using pip as follows:

    pip install -r requirements.txt 


# Usage
To use the script, simply run the twitter_scraping.py file using Python 3. You will be prompted to enter a search query for Twitter tweets, a maximum number of tweets to scrape, and a filename to save the scraped tweets as a JSON file. The script will then scrape the tweets that match the search query, save them as a JSON file with the specified filename, and log a message to indicate that the process is complete.

# Example
Here is an example of how to use the script:

    $ python twitter_scraping.py
    Enter a search query for Twitter tweets: crypto min_faves:100 lang:en until:2022-12-31 since:2022-12-01
    Enter the maximum number of tweets to scrape: 1000
    Enter a filename to save the scraped tweets as a JSON file: crypto_december2022.json

This will scrape up to 1000 English-language tweets containing the word "crypto" and with at least 100 likes, posted between December 1, 2022 and December 31, 2022, and save them as a JSON file named crypto_december2022.json. Once the scraping process is complete, a log message will be written to a file named scraping.log indicating how many tweets were scraped and where they were saved.

# Limitations
Please note that the Twitter scraping script may be subject to rate limits imposed by Twitter's API. This means that you may not be able to scrape a large number of tweets in a short period of time. Additionally, the script only works for publicly available tweets, so it may not be able to scrape tweets that are protected or otherwise inaccessible. Finally, please be aware that Twitter's terms of service prohibit automated scraping of their website, so use this script at your own risk.