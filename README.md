# sentiment-api-hum
A FastAPI app that takes a keyword, searches for recent tweets, and returns a sentiment score.

## Overview
I had two goals for this project:
1. Familiarizing myself with FastAPI as a way to quickly deploy a data model via a REST api endpoint.
2. Complete the development and production cycle all within a Docker container.

Goal 1:
This project was my first time working with the FastAPI package. I worked with Django in the past to develop a website but needed something more light-weight and faster. Coming from a data scientists perspective, I was looking for a framework that would allow me to quickly deploy a model that could be used by anyone via a REST api endpoint.
I was able to deploy a pre-trained sentiment-analysis model with Fast API and then generate a simple web-ui that could be accesed via URL. This created a self-serve consumption point for end-users. 

Goal 2:
Docker is an amazing tool that I have used in the past to quickly spin up databases and linux environments for development. Until this project I hadn't actually used a docker container to deploy an application. I chose Digital Ocean since they had good support for deploying docker containers and I had a free trial.
While there was a learning curve associated with using docker, I did find it easier to develop and deploy with docker vs trying to create the environment locally and then deploy the application in a production setting. 
