[![flake8 Lint](https://github.com/acdh-oeaw/eurotort/actions/workflows/lint.yml/badge.svg)](https://github.com/acdh-oeaw/eurotort/actions/workflows/lint.yml)
[![Test](https://github.com/acdh-oeaw/eurotort/actions/workflows/test.yml/badge.svg)](https://github.com/acdh-oeaw/eurotort/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/acdh-oeaw/eurotort/graph/badge.svg?token=OBVVMXQIX7)](https://codecov.io/gh/acdh-oeaw/eurotort)

# Eurotort - Database on European Tort Law

short description of the project

## install

* clone the repo
* change into the project's root directory e.g. `cd eurotort-app`
* create a virtual environment e.g. `virutalenv env` and activate it `source env/bin/activate`
* install required packages `pip install -r requirements_dev.txt`
* run migrations `python manage.py migrate`
* start the dev sever `python manage.py runserver`
* go to [http://127.0.0.1:8000](http://127.0.0.1:8000/) and check if everything works


## Docker

At the ACDH-CH we use a centralized database-server. So instead of spawning a database for each service our services are talking to a database on this centralized db-server. This setup is reflected in the dockerized setting as well, meaning it expects an already existing database (either on your host, e.g. accessible via 'localhost' or some remote one)

### building the image

* `docker build -t eurotort:latest .`
* `docker build -t eurotort:latest --no-cache .`


### running the image

To run the image you should provide an `.env` file to pass in needed environment variables; see example below:

* `docker run -it -p 8020:8020 --rm --env-file env.default --name eurotort eurotort:latest`

-----

This project was bootstraped by [djangobase-cookiecutter](https://github.com/acdh-oeaw/djangobase-cookiecutter)