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

**GET /challenges/**
Get all the registered challenges

Response:

```
{
  "challenges": [
    {
      "riddle_text": "Best human friend",
      "id": 1
    },
    {
      "riddle_text": "Composed by one oxygen atom and two hydrogen atom",
      "id": 2
    }
  ]
}
```

**GET /challenges/:challenge_id**
Get the riddle for a specific challenge

Response:
```
{
  "challenge": {
    "riddle_text": "Best human friend",
    "id": 1
  }
}
```

**POST /challenges/:challenge_id/solve**
Check if an attempt to solve the current challenge is valid.

Parameters:

* `attempt` **REQUIRED**: URL to the current attempt image

Response:

If the challenge is solved:
```
{
  "solved": true,
  "text": "GGWP"
}
```

If the challenge is not solved:

```
{
  "solved": false,
  "text": "Nice try!",
  "guessed": {
    "concepts": [
      {
        "id": "ai_mFqxrph2",
        "name": "cat",
        "value": 0.9651122,
        "app_id": "main"
      },
      {
        "id": "ai_SzsXMB1w",
        "name": "animal",
        "value": 0.95982313,
        "app_id": "main"
      },
      {
        "id": "ai_TJ9wFfK5",
        "name": "portrait",
        "value": 0.9448299,
        "app_id": "main"
      }
    ]
  }
}
```

