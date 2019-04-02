# Django Phonebook

This is the django phonebook app where user come do signup and then after email verification used this app to store his/her contacts.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You need a django project with app in same structure like i upload on git.


### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
	In terminal run this command : `. 	setup.sh`
	After that run  `redis-5.0.3/src/redis-server`
	open a new terminal 
	 Enter `python manage.py runserver`
```
End with an example of getting some data out of the system or using it for a little demo

## Running worker

```
celery -A proj worker -l info
```

## Running the tests

You can run the test by using just a command 

`./manage.py test`<br>

## Authors

* **Shahrukh Ijaz** - *Initial work* - [SHAHRUKH IJAZ](https://github.com/shahrukh-ijaz)




