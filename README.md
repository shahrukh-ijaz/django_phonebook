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
	After that run  `redis-5.0.4/src/redis-server`
	open a new terminal 
	 Enter `python manage.py runserver`
```
End with an example of getting some data out of the system or using it for a little demo

## Running worker

```
open a terminal, activate the virtual env and then run the below command:

celery -A phone_book worker -l info
```

## Running the tests

You can run the test by using just a command 

`./manage.py test`<br>


## REST API
```python\
# Login [POST]
http://127.0.0.1:8001/api/login?username=shahrukh-ijaz&password=shahrukh31
# profile [GET]
http://127.0.0.1:8001/api/profile
# profile [PUT]
http://127.0.0.1:8001/api/profile
# logout [GET]
http://127.0.0.1:8001/api/logout
# Contacts [GET]
http://127.0.0.1:8001/api/contacts
# Contacts [POST]
http://127.0.0.1:8001/api/contacts
parameter {
        "id": 21,
        "first_name": "222222",
        "last_name": "2",
        "note": "2",
        "dob": "2018-03-12",
        "user_id": 91
    }
# Contacts [PUT]
http://127.0.0.1:8001/api/contacts
parameter{
        "id": 21,
        "first_name": "222222",
        "last_name": "2",
        "note": "2",
        "dob": "2018-03-12",
        "user_id": 91
    }

```
[/api/login](https://choosealicense.com/licenses/mit/) 


## Authors

* **Shahrukh Ijaz** - *Initial work* - [SHAHRUKH IJAZ](https://github.com/shahrukh-ijaz)




