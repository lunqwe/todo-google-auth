# Todo application

The project implements the Todo management system. Also there is an ability to login using Google authentication. 

## Project Description

My project implements a todo task management system. Here you can do CRUD operations with todos.
The key feature of this project is my own realization of JWT. The reason is that django_allauth didn`t provide some flexibility I needed for this project.
Authentication system has been implemented using JWT + dj_rest_auth, and an authentication system through Google has also been implemented using its API.

## Instructions (to launch using Docker)

**Running the Application:**
   - To get the project files, use the following command:
     ```
     git clone https://github.com/lunqwe/zapplyai-task
	   cd zapplyai-task
     ```
   - To run the project,  use the following command (Docker required):
     ```
     docker-compose up --build
     ```

## Manual launch (clone project first, like described above)
If you want to launch the project manually, please note that Celery is set up using Docker (Redis is also running inside Docker). If you still wish to proceed, go ahead! :)


1. **Create and launch venv:**
   To create venv, use the following command:
	```
	python -m venv venv
	```
	Then use this command to launch your venv:
	```
	 venv\Scripts\activate # for windows
	 source venv/bin/activate # for macOS
	```
	
2. **Install dependencies**
To install dependencies, use ths command:
	```
	pip install req.txt
	```
3. **Choose database**:
	If you are running project locally, you have to change db settings.
	 To make it:
	1. Go to {project_folder}/config/settings.py
	2. Find commented local database, and uncomment it
	3. Comment docker db 
	
4. **Create migrations:**
	To make sure all migrations are there, use this command:
	```
	python manage.py makemigrations
	```
	Then use this command to apply migrations into your local project:
	```
	python manage.py migrate
	```
	4. **Run server**
	   
	To run server:
	```
	python manage.py runserver
	```
	5. **Tests**
	   
	To run tests:
	```
	python manage.py test
	```

5. **API Documentation:**

   - API documentation can be accessed via [localhost:8000/swagger/](http://localhost:8000/swagger/) (for local server)

7. **Google auth setup**

To setup your own google auth, create your client_id and secret (https://console.cloud.google.com/apis/), then go to .env file inside config directory and replace cilent_id and secret.

**Example**
```
...
cilent_id='your_client_id'
secret='your_client_secret'
...
```



