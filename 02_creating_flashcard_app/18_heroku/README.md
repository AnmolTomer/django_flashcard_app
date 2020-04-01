# Heroku - Intro and Heroku Toolbelt Setup

---

- We will be using [Heroku](https://www.heroku.com/) for web hosting.

- Heroku specializes in Web Frameworks like Django, RubyOnRails, Node etc.

- Cool thing is you aren't required to know anything about running web-servers, no DevOPS needed.

- Just push code to Heroku much like git and you are good to go.

- Follow the instructions on this [link](https://devcenter.heroku.com/articles/heroku-cli) to setup heroku CLI on your local development environment.

- After CLI, we create a Procfile, it is sort of a descriptive file that lets Heroku know what kind of app we have flask, django, ruby etc.

- Go to flash >> wsgi.py file and see `flash.settings` that means flash is the name of our app, so we enter that in Procfile.

- Gunicorn is a web-server. Up till now we were using light-weight webserver that comes with Django to run and debug our app.

- For production we need a better web-server. That's why we use gunicorn web server for our needs.

- `pip install gunicorn`
- `pip install django_heroku`
- `pip install dj_database_url`
- `pip install python-decouple`

- We are almost done. Now we need to tinker with our settings.py file to customise it for Heroku and that will be all.

---

## Change settings.py file for Heroku

- Add these to `settings.py`

```python
import django_heroku
import dj_database_url
from decouple import config
```

- Go to MIDDLEWARE list in `**settings.py**` and add the following:
  `'whitenoise.middleware.WhiteNoiseMiddleware',`

- At the bottom of the page add this as well:

```python
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(locals())
```

- Whitenoise is for static files, that's all I know that we need to know for now. Will update here in future on whitenoise.

- `pip freeze` to see everything that is installed in the virtual env. Copy and paste these into requirements.txt file to tell heroku what are the packages needed by website.

---

# Push Code to Heroku

---

- Sign up for Heroku and Log In

- Type `heroku login` and browser will open with heroku follow the instructions to log in to heroku on your terminal.

- `heroku create` to create an app.
