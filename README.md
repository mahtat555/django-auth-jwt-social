# Django authentification JWT/Social

**A simple Django project for implementing an authentication system with JWT and social networking.**

## Requirements

- python3.10+
- python3.10-venv


### Database

#### 1. PostgresSQL

```console
$ # Access the PostgresSQL
$ sudo -u postgres psql
postgres#

postgres# # Create a new user
postgres# CREATE USER user_name WITH ENCRYPTED PASSWORD 'password';
postgres# # Create the database for this user with the same name
postgres# CREATE DATABASE user_name;

postgres# # Create a database
postgres# CREATE DATABASE db_name;

postgres# # Update the settings
postgres# ALTER ROLE user_name SET client_encoding TO 'utf8';
postgres# ALTER ROLE user_name SET default_transaction_isolation TO 'read committed';
postgres# ALTER ROLE user_name SET timezone TO 'UTC';

postgres# # give the user access rights to the database
postgres# GRANT ALL PRIVILEGES ON DATABASE db_name TO user_name;
```

```console
$ pip install psycopg2-binary
```

.env

```bash
...

# Postgresql
#-----------

DB_CONNECTION=postgresql
DB_HOST=localhost
DB_PORT=5432
DB_DATABASE=db_name
DB_USERNAME=user_name
DB_PASSWORD=password

...
```

#### 2. MySQL

```console
$ # Log in as the root user
$ sudo mysql -uroot -p
mysql>

mysql> # Create a new user
mysql> CREATE USER 'user_name'@'localhost' IDENTIFIED BY 'password!';

mysql> # Create a database
mysql> CREATE DATABASE db_name;

mysql> # Give the user access rights to the database
mysql> GRANT ALL PRIVILEGES ON db_name.* TO user_name@'localhost';
```

```console
$ pip install mysqlclient
```

.env

```bash
...

# MySQL
#------

DB_CONNECTION=mysql
DB_HOST=localhost
DB_PORT=3306
DB_DATABASE=db_name
DB_USERNAME=user_name
DB_PASSWORD=password

...
```

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
