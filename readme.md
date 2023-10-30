# Bubble API

## Concept

The idea behind this app was meant to deal a problem that emerged during lockdown / shutdown within my bubble of friends. 
We wanted to keep track of a list of movies to watch together. 

This API is meant to serve an app that allows people to search for movies, add them to the list to watch, add an anticipaton rate. At the end it will generate an optimized list to help select the next movie hoepfully everybody will be happy to watch together.

## Stack

- Django Rest Framework
- PostgreSQL
- TMDB API

## Requirements

- Docker needs to be installed
    You can visit https://www.docker.com/get-started/

## Installation

- create the .env file `cp .env.example .env`
- read the .env file to see instruction to generate your SECRET_KEY
- create the docker-compose.yml `cp docker-compose.yml.example docker-compose.yml`

- `$ docker-compose build`
- `$ docker-compose up`

- connect to the bubble_api.web container `$ docker exec -it bubble_api.web /bin/bash`
- Migrate the db `python manage.py migrate`

Open `http://localhost:8000` in your browser to see the API