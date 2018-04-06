# ROMAL (Temporary name)

## Requirements


- PostgresSQL or SQLite
- Redis

## Developer setup


### Install pipenv

See https://docs.pipenv.org/#install-pipenv-today

### Setup environment

    pipenv install


## Starting the server

### Apply database migrations


    pipenv run python manage.py migrate

###Run the server

    pipenv run python manage.py runserver localhost:5000

Now the site is runnning and auto-reloading the sources

## Deployer tasks

### Adding a dependency

    pipenv install [DEPENDENCY]

### Updating the requirements file

    pipenv run pip freeze > requirements.txt