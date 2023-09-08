### Prerequisites

- Python 3.10

### Project Installation

- Install `postgres` docker.

- Go to root of this project.

- Run the following command to migrate database schema to the docker database

```
$ yarn db:migrate
or
$ npx prisma migrate dev --name init_db 
```
- Or

```
$ npx prisma migrate dev --name init_db 
```

- Run the following command to seed 3 three dummy users in the database.

```
$ yarn db:seed
```

- Create .env file and copy the contents of .env.example
- Install `pipenv` a global python project using:

```
$ pip3 install pipenv
```

- Activate virtual environment using

```
$ python3 -m pipenv shell
```

- To install from pipfile:

```
$ pipenv install
```

```
$ pip install -r requirements.txt
```

- Create a log folder
- Run flask app using

```
$ python run.py
```

Then the flask applucation should be running on `http://127.0.0.1:5000`

