from re import template
from fastapi import FastAPI, Query, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.twitterapi import *
from app.texttools import *
from app.schemas import *
from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent

#declare app
app = FastAPI()

app.mount("/static/", StaticFiles(directory=str(BASE_DIR/"static")),name="static")

#set templates directory
templates = Jinja2Templates(directory=str(BASE_DIR/"templates"))


#Get methods
@app.get("/",response_class=HTMLResponse)
async def get_index(request: Request):
	return  templates.TemplateResponse("base.html", {"request":request}) 

@app.get("/form")
def form_post(request: Request):
	result = ""
	return templates.TemplateResponse("index.html",context={'request':request,'result':result})

@app.post("/form")
def form_post(request: Request, term: str = Form(...)):
	result = get_results(term)
	return templates.TemplateResponse("index.html",context={'request':request,'result':result})


@app.get("/term/")
def get_results(term: str | None =  Query(default = None,min_length=3, max_length=25)):
	try:	
		if term:
			raw_results = searchTweets(term)
			processed_results = [process_text(tweet) for tweet in raw_results]

			sentiment = get_avg_sentiment(processed_results)	
			keywords = get_keywords(processed_results,5)

			results = {"sentiment" : sentiment[0],
				"score": sentiment[1],
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


	
	
