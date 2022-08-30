FROM python:3.10

WORKDIR /myfastapi

COPY ./requirements.txt /myfastapi/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /myfastapi/requirements.txt
RUN python -m nltk.downloader punkt stopwords vader_lexicon

COPY ./app /myfastapi/app

CMD ["uvicorn", "app.main:app","--host","0.0.0.0","--port","80"]