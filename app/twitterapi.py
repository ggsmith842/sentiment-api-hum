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
  except:
    error_message = "An error occured"
    return error_message
   


