# Setting Up Development Environment

- Get python installer from this [link](https://www.python.org/downloads/)

- Get VSCode Editor from this [link](https://code.visualstudio.com/)

- Get git from this [link](https://git-scm.com/) avoid git for windows first google link.

## Creating a venv (Virtual Environment)

A virtual environment is sort of a fenced garden that separates packages and their respective versions used in one project,
from other project and different versions of same packages. It helps to avoid version conflict between different packages.
So it's best practice to have virtual environment in Python. We will be using venv.

- Create a new venv by typing

```python
python -m venv virtualEnvName
```

- On windows activate by typing following:

```python
#For Unix/Linux
source env/bin/activate
#For Windows for an environment named env
.\flashcard_app\Scripts\activate
# To deactivate
deactivate
```

## Install Django and start project

- Now everytime you want to run the code, you need to be inside the parent directory where venv folder in this case flashcard_app was created.

- Use python installation program pip to install django by typing `pip install django` in terminal

- Next, inside the django_flashcard_app directory we create a django project by typing `django-admin.py startproject flash`

- If `django-admin.py startproject flash` fails try `django-admin.exe startproject flash`

- cd to project name i.e. flash in our case.

- On going inside flash directory we see there is flash/ directory inside flash/ and manage.py file.

- All the work now will happen from inside this flash/ directory. Just do a simple ls and if you see manage.py in current dir you are at right address.

## Run the web-server

- Django comes with its own little built-in server, allows us to run the server/project in a web browser and check it locally.

- From now on all the commands will be of the format `python manage.py <command>`

- Django Tutorial Polling app - [Link](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)

## Migrate the Database

- We won't be using a DB as it is not needed for this project but, Django comes with a very basic DB called SQLite.

- Django also comes with an administration area, a backend sort of interface that allows us to connect to DB.

- To use a DB we have to create a migration and we have to push the migration.

- When Django is installed there are some migrations that comes with admin area, that needs to be pushed to the server, else errors are thrown.

- To do these migrations what we do is `python manage.py migrate`

- `python manage.py runserver` >> To go to admin area : http://localhost:8000/admin/, it will ask you to login. To create login do the following:

- `winpty python manage.py createsuperuser` >> Run server >> log in >> You will see admin area.

- We migrate the server so that admin area can be accessed. Not of much use in our case.
