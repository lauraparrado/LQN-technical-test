 # SW API GraphQL

## Requirements
* [Python](https://www.python.org/) (realizado en python 3.8)
* [Django](https://github.com/django/django)
* [Django Filter](https://github.com/carltongibson/django-filter)
* [Django model utils](https://github.com/jazzband/django-model-utils)
* [Graphene](https://github.com/graphql-python/graphene-django)
* [.EVN](https://github.com/theskumar/python-dotenv)

## Setup

Clone the project
```
git clone https://github.com/lauraparrado/LQN-technical-test.git
```

Move into de repo and install dependencies
```
pip install -r requirements.txt
```

Run migrations and load fixtures
```
python manage.py migrate
python manage.py load_fixtures
```
### Running logical exercises of the test
Run exercise 1
```
python manage.py logic_exercise_1
```
Run exercise 2
```
python manage.py logic_exercise_2
```
### Running the server
```
python manage.py runserver
```
If you want to check it out, access the graphi explorer here: `127.0.0.1:8000/explore`.

The service should be available in the URL: `127.0.0.1:8000/graphql`.

### Runing the tests
```
python manage.py test
```

### Test server

If you want to check it out, access the graphi explorer here: `https://prueba-laura-lqn.herokuapp.com/explore`.

The service should be available in the URL: `https://prueba-laura-lqn.herokuapp.com/graphql`.