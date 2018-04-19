# ROMAL (Temporary name)

## Requirements


- PostgresSQL or SQLite
- Redis

## Developer setup


### Install pipenv

See https://docs.pipenv.org/#install-pipenv-today

### Get a Clarifai API key

You can create an API key on your [clarifai dashboard](https://clarifai.com/developer/account/keys).

The API key must have the following scopes:

* Models:Get
* Predict

Once created add this key to your `.env` file:

```bash
echo "CLARIFAI_API_KEY=<YOUR_CLARIFAI_API_KEY>" >> .env
```

### Setup environment

    pipenv install


## Starting the server

### Apply database migrations


    pipenv run python manage.py migrate

### Run the server

    pipenv run python manage.py runserver localhost:5000

Now the site is runnning and auto-reloading the sources

## Deployer tasks

### Adding a dependency

    pipenv install [DEPENDENCY]

### Updating the requirements file

    pipenv run pip freeze > requirements.txt

### Available routes

**/recognition/recognize**
Parameters:

* `image` (required): URL to an image
* `model` (default: `general-v1.3`): model used to predict the image content
