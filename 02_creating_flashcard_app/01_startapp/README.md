# Startapp

- So we've migrated our server and installed all the things, next thing is we want to get rid of default django localhost:8000 page.
- In django first thing we need to do is start an app. Django is all about apps. Everytime we want to do something with django project, we have to create an app.

- We have already created a project, and inside that project we need to create an app.
- Go to the directory which contains manage.py and type this: `python manage.py startapp website`
- You'll see a website named folder created in the same directory.

- Now we have created the app, now we need to tell our project that we have made an app and inform this to the project.
- To do so, go to flash directory and in there go to `settings.py`
- This settings.py file will be used from time to time to add and modify stuff, right now no need to dive deep into the details of it.
- In settings.py file inside flash directory in `INSTALLED_APPS` section we need to register our app.
- Type in `'website'` in the list `INSTALLED_APPS` and we are ready to go to next step.
