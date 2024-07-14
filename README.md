# Test task for Zapply AI

The project implements the Todo management system. 

*Note: I submitted a .env file in addition to my project.*

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

6. **Google auth setup**
To setup your own google auth, create your client_id and secret (https://console.cloud.google.com/apis/), then go to .env file inside config directory and replace cilent_id and secret.

**Example**
```
...
cilent_id='your_client_id'
secret='your_client_secret'
...
```
## Project Description

My project implements a todo task management system.
Also, a user authentication system has been implemented using JWT + dj_rest_auth, and an authentication system through Google has also been implemented using its API.

An example of how authorization via Google works can be found at this link (when the server is running locally):
http://localhost:8000/google-auth-test/

##Dev notes
####Discontinuation of django-allauth:
django-allauth works well only with Django, so I opted for django-rest-auth,
which handled both Google authentication and regular authentication quite well. However, due to recent updates
in Google's authentication methods, it no longer meets the required functionalities. That's why I decided to implement my own
authentication functionality (described below).

####I have implemented authorization using djangorestframework-simplejwt.
I made this decision for several reasons:
1. **Ease of use**: drf-simplejwt is very convenient and easy to use.
2. **Flexibility**: With this library, I created code that can be easily modified and adapted
to fit the project needs.

Additionally, I used several views from django-rest-auth.

####Google Authorization:
Due to recent updates from Google, the django-rest-auth library, unfortunately,
is not functional (its built-in serializer requires access_token, code, and id_token, whereas in the new version of Google authentication, the API only provides id_token).
That's why I decided to create my own view function (GoogleAuthView), which works successfully in my project in conjunction with simple-jwt (another reason to use drf-simplejwt :) ).

In addition, I implemented some JavaScript logic to test the functionality of my endpoint, as I mentioned above

####Celery:
I thought it would be cool if users received a notification some time before their Todo deadline, so I added Celery.

####PostgreSQL instead of SQLite:
I decided that adding PostgreSQL to my project would be great :)

Docker & docker-compose:
I thought it would be a good practice to include these tools in my project.

Swagger:
I added swagger and redoc to my project to better understand its structure (using
the drf-yasg library).

