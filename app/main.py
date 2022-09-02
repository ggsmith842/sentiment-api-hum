from fastapi import FastAPI, Query
from app.twitterapi import *
from app.texttools import *
from app.schemas import *

#declare app
app = FastAPI()

#Get methods
@app.get("/")
async def get_index():
	return {"message":"Landing Page Goes Here"}

@app.get("/term/")
async def get_results(term: str | None =  Query(default = None,min_length=3, max_length=25)):
	try:	
		if term:
			raw_results = searchTweets(term)
			processed_results = [process_text(tweet) for tweet in raw_results]

			sentiment = get_avg_sentiment(processed_results)	
			keywords = get_keywords(processed_results,10)

			results = {"sentiment" : sentiment,
				"keywords":keywords
			}
			return results
		else:
			return {"message":"nothing to seach"}
	except Exception as e:
		return {"error":e}

@app.get("/tweets/")
async def get_tweets(term: str | None = Query(default=None, min_length=3, max_length=25)):
	if term:
		raw_results = searchTweets(term)
		return raw_results
	else:
		return {'message':'no results'}

@app.get("/trends/")
async def get_trends():
	try:
		response = call_trends()
		return response
	except:
		return {'message':'An error occured'}


#POST
@app.post("/items/")
async def create_item(item: Item):
	item_dict = item.dict()
	if item.tax:
		price_with_tax = item.price + item.tax
		item_dict.update({"price_with_tax": price_with_tax})
	return item_dict


	
	
