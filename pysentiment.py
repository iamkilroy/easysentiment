import boto3
import tweepy

// Get your API keys from your Twitter developer dashboard
api_key = 'twitter-api-key'
api_secret = 'twitter-secret-api-key'
access_token = 'twitter-access-token'
access_token_secret = 'twitter-access-token-secret'

// Twitter Auth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Define the search term and the date_since date as variables
stock_symbol = '$tsla'
since_date = '2020-10-08'

# Get stock tweets
tweets = tweepy.Cursor(api.search,
              q = stock_symbol,
              lang = 'en',
              since = since_date).items(10)

// Get Comprehend client
client = boto3.client('comprehend')

# Score and print tweets
for tweet in tweets:
    response = client.detect_sentiment(Text = tweet.text, LanguageCode = 'en')
    print(response, tweet.text)
