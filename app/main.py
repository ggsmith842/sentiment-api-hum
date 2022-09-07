from fastapi import FastAPI, Request, Form, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.twitterapi import *
from app.visuals import *
from app.texttools import *
from pathlib import Path
from datetime import date

BASE_DIR = Path(__file__).resolve().parent

#declare app
app = FastAPI()

app.mount("/static/", StaticFiles(directory=str(BASE_DIR/"static")),name="static")

#set templates directory
templates = Jinja2Templates(directory=str(BASE_DIR/"templates"))

@app.get("/")
def form_post(request: Request):
	try:
		return templates.TemplateResponse("index.html",context={'request':request})
	except:
		return templates.TemplateResponse("404.html",context={'request':request})

@app.post("/")
def form_post(request: Request, term: str = Form(...,min_length=3,max_length=25)):
	try:
		result = get_results(re.sub('\W','',term))
		plot_sentiment(result['score'])
		return templates.TemplateResponse("results.html",context={'request':request,'result':result, 'term':term})
	except:
		return templates.TemplateResponse("404.html",context={'request':request})

@app.get("/visual", response_class=HTMLResponse)
def post_gauge(request: Request):
	try:
		return templates.TemplateResponse("gauge.html", {"request":request})
	except:
		return templates.TemplateResponse("404.html",context={'request':request})

@app.get("/term/")
def get_results(term: str | None =  Query(default = None,min_length=3, max_length=25)):
	try:	
		if term:
			raw_results = searchTweets(term)
			if not raw_results:
				return Exception
			else:
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
def get_tweets(term: str | None = Query(default=None, min_length=3, max_length=25)):
	if term:
		raw_results = searchTweets(term)
		return raw_results
	else:
		return {'message':'no results'}

@app.get("/trends/")
def get_trends(request: Request):
	curr_date = date.today().strftime("%m/%d/%y")
	try:
		result = call_trends()
		return templates.TemplateResponse("trends.html", context={'request':request,'result':result, 'date':curr_date})
	except Exception as e:
		return templates.TemplateResponse("404.html",context={'request':request})

@app.get("/error")
def get_error(request: Request):
		return templates.TemplateResponse("404.html",context={'request':request})

@app.get("/about/")
def get_about(request: Request):
		return templates.TemplateResponse("about.html",context={'request':request})
