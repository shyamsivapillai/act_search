
# act_search
An application to search through sections in Indian legislations. 

## Run on local

The repository mainly consists of 3 components:

 1. Frontend - React
 2. Backend - Flask
 3. Database - Postgres

You can choose to run these individually or simply use `docker-compose` to run. 

### Running the services individually

1. Install Postgres on your system and create a database called `legal_acts_db`
2. Install the latest version of node ( currently LTS is v18.x )
3. Install Python >= 3.8
4.  Clone the repo
5. `cd` into the repo
6. To run the backend: 
	a. `cd api`
	b. `pip install -r requirements.txt`
	c. `flask run`
7. To run the frontend:
	a. `cd fe`
	b. `npm i -g yarn` if you do not have `yarn` in your system
	c. `yarn start`

Point your browser to `http://localhost:3000/` and you should be able to view the application

### Running the application via docker-compose

1. Install Docker and Docker Compose on your system
2. Clone the repo
3. `cd` into the repo
4. `docker-compose up`

Point your browser to http://localhost:3000/ and you should be able to view the application

## Extending the legislations

Currently the application has somewhere over a 1000 legislations in the `api/data` directory. The legislations are stored as `.json` files. If you would like to add more legislations to the project, you can condense a legislation into a dictionary with every section representing a `key` and it's corresponding value representing it's `value` . Eg:

`{"1": "1.Introduction: This act aims to ....", "2": "2.Definitions: ..."}`

Every legislation also needs to have a key called "name" which will refer to the name of the legislation.

Once the dictionary is created, save it as a json file with a short and meaningful name. Restarting the API service / docker service should pick the new file(s) and store it in the database, making it available for future searches.
