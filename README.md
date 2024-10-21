
### database
* docker compose up

### python
* source venv/Scripts/activate
* pip install -r requirements.txt

### admin
* username: admin
* password: admin
* http://localhost:8000/admin/login/?next=/admin/

### new user registration
* http://127.0.0.1:8000/auth/users/

### token create
* http://127.0.0.1:8000/auth/token/login/

### testing
* cd littlelemon
* pytest

### run django
* python manage.py runserver

### module 4 goals
* [complete] ~~Does the web application use Django to serve static HTML content?~~
* [complete] ~~Has the learner committed the project to a Git repository?~~
* [complete] ~~Does the application connect the backend to a MySQL database?~~
* [complete] ~~Are the menu and table booking APIs implemented?~~
  * http://localhost:8000/api/menu-items/
  * http://localhost:8000/api/booking/
* [complete] ~~Is the application set up with user registration and authentication?~~
* [complete] ~~Does the application contain unit tests?~~
* [complete] ~~Can the API be tested with the Insomnia REST client?~~

### module 4 tasks
* Does the web application use Django to serve static HTML content?
  * http://localhost:8000/
* Has the learner committed the project to a Git repository?
  * https://github.com/cjhilyard/littlelemon
* Does the application connect the backend to a MySQL database?
  * yes
* Are the menu and table booking APIs implemented?
  * http://localhost:8000/api/menu-items/
  * http://localhost:8000/api/booking/* 
* Is the application set up with user registration and authentication?
  * http://127.0.0.1:8000/auth/users/
* Does the application contain unit tests?
  * yes under tests folder
* Can the API be tested with the Insomnia REST client?
  * yes