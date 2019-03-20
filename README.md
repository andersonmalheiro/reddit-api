# Fake Reddit API

This is a simple REST API that mimics some of Reddit's features, like create comunities, posts and comments;

## Running
All the commands below are made on the terminal:

- Clone this repo with `git clone https://github.com/andersonmalheiro/reddit-api.git`;
- Change directory to the project's root folder with `cd reddit-api`;
- Create a virtual environment with `python3 -m virtualenv <ENV_NAME>`;
- Activate the environment with `source <ENV_NAME>/bin/activate`;
- Install the project's dependencies with `pip install -r requirements.txt`;
- Make the database migrations with `python manage.py migrate`;
- Start the server with `python manage.py runserver`;

- The server will run on http://localhost:8000/
