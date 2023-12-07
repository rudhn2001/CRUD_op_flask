
# CRUD operations using Flask, RestAPI and Postgresql

The following project shows a demonstration of CRUD operations where postgresql database is used and the data is sent through RestAPI. This is done in Flask Framework.

The project contains the following: 

1. requirements.txt :  contains all the dependencies of the project. We would need three

```bash
  flask
  psycopg2-binary
  Flask-SQLAlchemy
```
we would also need Docker desktop for dockers, postman for checking the requests at the endpoints, and postgresql for Database. I used TablePlus which provides a GUI for the Postgres.

psycopg2-binary is to make connection with postgres db 

Flask-SQLAlchemy is the ORM to make queries for db

2. App.py : contains the logic and endpoints for application
* Here we create the Table named as ``orders`` consisting of columns : order_id, customer_name, email, street, city, state, postal_code, prodict_name, quantity, order_date, priority.
- 

3. DockerFile : for docker containers

4. docker-compose.yml : to define the services
in docker-compose, the ``flask_app`` is the application dockerized,
``flask_db`` is the postgres container to store data.  
- They both are the services to be run. ``image`` is the name of image that has to be changed accordingly with docker username (Format: "dockerhub_Username"/crud_op) . 
- we use two ports: "4000" for flask_app and "5432" for postgres.
``environment`` is to define environment variables. Here we use "DB_URL" where postgres in the URL is the used for db, user and password.

## Postgresql specifications : 
- hostname : localhost
- port no. : 5432
- username : postgres
- password : postgres
- database : postgres

## Deployment

To deploy this project : 

Step 1 : install the requirements

```bash
  pip install -r requirements.txt
```

Step 2 : run the postgres-container

```bash
  docker compose up -d flask_db
```

the -d is to run container in background, or it can be seen through Docker desktop also.

To check if container is running, type : 

```bash
  docker ps -a
```

which shows all containers running in docker

Step 3 : test the Database connections whether the database is working in background. we can use TablePlus application for more better GUI.

Step 4 : Build and run the flask Application, where docker-compose.yml is stores

```bash
  docker compose build
```

This will build a flask_app image, with name defined in "image" value

to check if the image has been built successfully, type:

```bash
  docker images
```

Step 6 : run a container based on the image built,

```bash
  docker compose up flask_app
```

## Testing

To Test the application, we use Postmanfor endpoints

1. Making a GET request to 
``
  localhost:4000/orders
`` 
gives an empty array at first because table is empty

2. Making a POST request to `` localhost:4000/orders ``

with json format as 
```bash
  {   
    "customer_name": "tiffany",
    "email": "tiffany0@hc360.com",
    "street": "Rajajinagar",
    "city": "Mangalore",
    "state": "Karnataka",
    "postal_code": 575755,
    "product_name": "Cheese - Provolone",
    "quantity": 1,
    "order_date": "06/10/2023",
    "priority": 1
    }
``` 
3. To get all users, make a GET request to `` localhost:4000/orders ``

4. To get a specific user, make a GET request and type the order_id along with users/ in `` localhost:4000/orders/<order_id> ``

5. To update a user, make a PUT request along with order_id specified in `` localhost:4000/orders/<order_id> `` and then change the JSON data. Then make a GET request to check the updated data

6. To delete the user, make a DELETE request to `` localhost:4000/orders/<order_id> `` . Then make a GET request to check the updated data