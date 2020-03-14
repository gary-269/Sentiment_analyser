import re

import tweepy
from nltk.corpus import stopwords
from textblob.tokenizers import word_tokenize
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, api
from tweepy import Stream
import json
import pandas as pd
import csv

import string

import twitter_credentials

# Columns for CSV file
COLS = ['Id', 'created_at', 'text', 'name', 'location', 'followers-count', 'friends_count', 'retweet_status']

# HappyEmoticons
happy_emoticons = {':-)', ':)', ';)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}', ':^)', ':-D', ':D', '8-D',
                   '8D', 'x-D', 'xD', 'X-D', 'XD', '=-D', '=D', '=-3', '=3', ':-))', ":'-)", ":')", ':*', ':^*', '>:P',
                   ':-P', ':P', 'X-P', 'x-p', 'xp', 'XP', ':-p', ':p', '=p', ':-b', ':b', '>:)', '>;)', '>:-)', '<3'}

# Sad Emoticons
sad_emoticons = {':L', ':-/', '>:/', ':S', '>:[', ':@', ':-(', ':[', ':-||', '=L', ':<', ':-[', ':-<', '=\\', '=/',
                 '>:(', ':(', '>.<', ":'-(", ":'(", ':\\', ':-c', ':c', ':{', '>:\\', ';('}

# Emoji patterns
emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)

# combine sad and happy emoticons
emoticons = happy_emoticons.union(sad_emoticons)


def clean_tweets(tweet):
    stop_words = set(stopwords.words('english'))
    stop_words.add('\\n')
    word_tokens = word_tokenize(tweet)
    # after tweepy preprocessing the colon symbol left remain after removing mentions
    tweet = re.sub(r':', '', tweet)
    tweet = re.sub(r'‚Ä¶', '', tweet)
    # replace consecutive non-ASCII characters with a space
    tweet = re.sub(r'[^\x00-\x7F]+', ' ', tweet)
    # remove emojis from tweet
    tweet = emoji_pattern.sub(r'', tweet)
    # remove url pattern
    tweet = re.sub(r'^https?:\/\/.*[\r\n]*', '', tweet, flags=re.MULTILINE)
    # tweet.decode('ascii', 'ignore')
    # filter using NLTK library append it to a string
    strng = ""
    filtered_tweet = [w for w in word_tokens if not w in stop_words]

    # filtered_tweet = []
    # # looping through conditions
    # for w in word_tokens:
    #     # check tokens against stop words , emoticons and punctuations
    #     if w not in stop_words and w not in emoticons and w not in string.punctuation:
    #         filtered_tweet.append(w)
    return filtered_tweet
    # print(word_tokens)
    # print(filtered_sentence)return tweet


tweet_check_list = []


class StdOutListener(StreamListener):

    def on_data(self, raw_data):
        # print("--------------------------------------------------------------------------------------")
        try:
            json_raw_data = json.loads(raw_data)
            file1 = open("Raw_tweets2.txt", "a")
            file1.write(raw_data)
            file1.close()
            if "retweeted_status" in json_raw_data and "extended_tweet" in json_raw_data["retweeted_status"]:
                tweet = json_raw_data["retweeted_status"]["extended_tweet"]["full_text"]
            else:
                tweet = json_raw_data["text"]
            # print(tweet)
            createdAt = json_raw_data["created_at"]
            location = json_raw_data["user"]["location"]
            # print(createdAt)
            # print(location)
            filtered = clean_tweets(tweet)
            newTweet = ""
            for tokens in filtered:
                newTweet = newTweet + " " + tokens
            # print(*all_tweets, sep="\n")
            if newTweet not in tweet_check_list:
                tweet_check_list.append(newTweet)
                csvWriter.writerow([createdAt, newTweet, location])
        except BaseException:
            pass
        # print("Processed Tweet:" + newTweet)
        # print("tweet")
        # print(*tweet_check_list, sep="\n")
        # csvWriter.writerow([createdAt,, location])
        return True

    def on_error(self, status_code):
        print(status_code)


if __name__ == "__main__":
    # Accessing twitter credentials
    listener = StdOutListener()
    auth = OAuthHandler(twitter_credentials.api_key, twitter_credentials.api_secret_key)
    auth.set_access_token(twitter_credentials.access_token, twitter_credentials.access_token_secret)
    stream = Stream(auth, listener)
    api = tweepy.API(auth)
    # Writing tweets to a csv file
    csvFile = open('Day6.csv', 'a')
    csvWriter = csv.writer(csvFile)
    # csvWriter.writerow(["Created At", "Text", "Location"])
    stream.filter(languages=["en"],
                  track=["CAA", "NRC"])
    csvFile.close()
