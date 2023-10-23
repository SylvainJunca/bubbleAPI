# Bubble API



## How to install

- create the .env file `cp .env.example .env`
- read the .env file to see instruction to generate your SECRET_KEY
- create the docker-compose.yml `cp docker-compose.yml.example docker-compose.yml`

- `$ docker-compose build`
- `$ docker-compose up`

- connect to the bubble_api.web container `$ docker exec -it bubble_api.web /bin/bash`
- Migrate the db `python manage.py migrate`

Open `http://localhost:8000` in your browser to see the API