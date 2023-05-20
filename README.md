# Django authentification JWT/Social

**A simple Django project for implementing an authentication system with JWT and social networking.**

## Requirements

- python3.10+
- python3.10-venv


## Usage

### Build the project by using python-venv

```bash
$ # Project root folder
$ mkdir django-auth-jwt-social
$ cd django-auth-jwt-social

$ # Clone the repo
$ git clone git@github.com:Weelite/django-auth-jwt-social.git .
$ # OR
$ # Pull from Github
$ git pull

$ # # Create isolated Python environment
$ python -m venv venv
$ source venv/bin/activate

$ # Install the required libraries
$ pip install -r requirements.txt

$ # Set up the project configuration
$ cd src
$ cp .env.example .env
$ # Make sure to update/provide the configuration on .env file

$ # Run the migrations
$ python manage.py migrate
$ pythom manage.py collectstatic

$ # Start the Server
$ python manage.py runserver
```
