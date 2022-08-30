import re
from statistics import mean
from math import floor
from rake_nltk import Rake
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

def process_text(text):
  stop_words = set(stopwords.words('english'))
  clean_text = " ".join(re.findall('\w{3,}',text))
  clean_text = re.sub(r"https",'',clean_text)
  word_tokens = word_tokenize(clean_text)
  filtered_text = " ".join([word for word in word_tokens if word not in stop_words])
  
  return filtered_text

def get_keywords(sentences: list,topn:int = 5):
    '''
    Given a list of strings, return the top keywords that are at least 4 letters long
    '''        
    r = Rake()
    r.extract_keywords_from_sentences(sentences)
    r.get_ranked_phrases_with_scores()
    keywords = r.get_ranked_phrases()[0].split(" ")
    avg_keyword_len = floor(mean([len(i) for i in keywords]))
    best_keywords = [i for i in keywords if len(i)>avg_keyword_len and len(i)>3]
    return best_keywords[:topn]

#get sentiment
def get_avg_sentiment(tweets):
    sia = SentimentIntensityAnalyzer()

    term_sentiment = round(mean([sia.polarity_scores(tweet)['compound'] for tweet in tweets ]),2)

    if term_sentiment < -0.33:
        return ("negative", term_sentiment)
    elif term_sentiment > 0.33:
        return ("positive", term_sentiment)
    else:
        return ("neutral",term_sentiment)