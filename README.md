# Cocktail website
Powered by Django & Python

## General idea

This is an open website for everyone who is into cocktail world.<br/>
There is no need to register or login to see the cocktail recipes.<br/>
Register, login with your new account and upload your favorite cocktails!<br/>
Go to * [Live] version. (Still pending...)

## Fork github:

You can simply fork and use website without anything but<br/>
If using PyCharm, create new project,<br/>
Clone Git<br/>
`$ pip install django`<br/>
`$ python manage.py runserver`<br/>
##-------------------------------------------------------------------------
##Or the other way:
## Install Docker

Before running the server, install docker.

Latest version(not necessary):
* [installing docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04)
* [installing docker compose](https://docs.docker.com/compose/install/)

Older version apt-get:
* [installing docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04)
* `$ sudo apt-get install docker-compose`

## Useful Commands

* Install virtual environment<br />
`$ pip install pipenv`

* Run virtual environment<br />
`$ pipenv shell`

* Install pipfile, pipfile.lock, requirements.txt at once<br />
`$ pipenv install`

* Check if all requirements are installed<br />
`$ pip list`

* To start project you must make migrations<br />
`$ python (or python3) manage.py makemigrations`<br />
`$ python (or python3) manage.py migrate (will migrate all at once)`

* Create SuperUser (admin)<br />
`$ python manage.py createsuperuser`

* Run docker locally<br />
`$ docker-compose up -d`

* List running docker containers
`$ sudo docker ps`

* Run server<br />
`$ python manage.py runserver`

## Links

* [Live]
