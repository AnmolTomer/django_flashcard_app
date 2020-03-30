# Creating an URLs.py file

- After adding the app to the project >> settings.py list of INSTALLED_APPS, next thing to do is create urls.py file.

- urls.py file is made for the project i.e. exists inside the flash directory but for us in website directory there isn't any urls.py file.

- We will create urls.py file for website now. This file allows us to create urls for our project.

- Say you have `localhost:8000/contact.html` this is an URL, and we have to define it in some file, that file is urls.py.

- Create a new file `urls.py` inside the website directory, copy the stuff from `flash>> urls.py` into `website >> urls.py`

- Remove the following as we won't be needing these:

```python
from django.contrib import admin
path('admin/', admin.site.urls),
```

- Now we have `website >> urls.py` file we need to link it with `project (flash) >> urls.py` file, to do so:

```python
from django.urls import path,include

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',include('website.urls')), # References urls.py inside webste directory.
]
```
