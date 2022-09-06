import requests
import os
from dotenv import load_dotenv

load_dotenv()

def searchTweets(search_term:str):
  '''
  Return tweets for a keyword seach term. 
  '''
  url = "https://api.twitter.com/2/tweets/search/recent?max_results=25&expansions=referenced_tweets.id&tweet.fields=text&query=lang%3Aen%20"+search_term

  payload={}
  headers = {
    'Authorization': os.getenv("BEARER_TOKEN"),
    'Cookie': 'guest_id=v1%3A165292464833657250; guest_id_ads=v1%3A165292464833657250; guest_id_marketing=v1%3A165292464833657250; personalization_id="v1_D50leSEsdlQN9nTvwQ6B+g=="'
    }

  try:
    response = requests.request("GET", url, headers=headers, data=payload).json()['includes']['tweets']
    tweets = [i['text'] for i in response]
    return tweets
  except Exception as e:
    error_message = f"An error occured in searchTweets(): {e}"
    return error_message
   

def call_trends():
  url = "https://api.twitter.com/1.1/trends/place.json?id=23424977"
  headers = {
  'Authorization': os.getenv("BEARER_TOKEN"),
  'Cookie': 'guest_id=v1%3A165292464833657250; guest_id_ads=v1%3A165292464833657250; guest_id_marketing=v1%3A165292464833657250; personalization_id="v1_D50leSEsdlQN9nTvwQ6B+g=="'
  }

  try:
    response = requests.request("GET",url,headers=headers).json()[0]['trends']
    response.sort(key=lambda x:0 if x["tweet_volume"] is None else x["tweet_volume"],reverse=True)
    results = [trend['name'] for trend in response]
    return results
  except Exception as e:
    error_message = f"An error occured in call_trends(): {e}"
    return error_message