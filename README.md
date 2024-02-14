# Database Project Starter

This is a starter project for you to use to start your Python database projects.

There are two videos to support:

- [A demonstration of setting up the project](https://youtu.be/8dBADUN8gdg?t=0s)
- [A walkthrough of the project codebase](https://www.youtube.com/watch?v=8dBADUN8gdg&t=287s)

## Setup

```shell
# Clone the repository to your local machine
; git clone git@github.com:makersacademy/databases-in-python-project-starter.git YOUR_PROJECT_NAME

# Or, if you don't have SSH keys set up
; git clone https://github.com/makersacademy/databases-in-python-project-starter.git YOUR_PROJECT_NAME

# Enter the directory
; cd YOUR_PROJECT_NAME

# Install dependencies and set up the virtual environment
; pipenv install
# Read below if you see an error with `python_full_version`

# Activate the virtual environment
; pipenv shell

# Create the database
; createdb YOUR_PROJECT_NAME

# Open lib/database_connection.py and change the database name to YOUR_PROJECT_NAME
; open lib/database_connection.py

# Run the tests
; pytest

# Run the app
; python app.py
```

```mermaid
sequenceDiagram
    participant t as terminal
    participant app as Main program (in app.py)
    participant ar as AlbumRepository class <br /> (in lib/album_repository.py)
    participant db_conn as DatabaseConnection class in (in lib/database_connection.py)
    participant db as Postgres database

    Note left of t: Flow of time <br />⬇ <br /> ⬇ <br /> ⬇

    t->>app: Runs `python app.py`
    app->>db_conn: Opens connection to database by calling 'connect' method on DatabaseConnection
    db_conn->>db_conn: Opens database connection using PGSQL and stores the connection
    app->>ar: Calls 'all' method on AlbumRepository
    ar->>db_conn: Sends SQL query by calling 'execute' method on DatabaseConnection
    db_conn->>db: Sends query to database via the open database connection
    db->>db_conn: Returns a list of dictionaries, one for each row of the albums table

    db_conn->>ar: Returns a list of dictionaries, one for each row of the albums table
    loop
        ar->>ar: Loops through a list and creates an Album object object for every row
    end
    ar->>app: Returns a list of Album objects
    app->>t: Prints list of albums to terminal
```
