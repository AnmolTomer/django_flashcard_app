# Understanding URLs, Views and Templates

---

- Everytime we create a webpage with Django it is a three step process. We need **View**, **URL** and we need a **template** file.

- Create a new folder named templates inside website folder.

- Everytime we create a HTML file for a webpage it will be stored inside templates folder.
- Inside templates make home.html and after that go to urls.py of website directory and add the following

```python
urlpatterns = [path('', views.home, name= "home")]
#Example of path
path(​route, view, name="'index'"​)
```

- For views.home in urlpatterns above we need to import in urls.py in the following manner `from . import views`

- In view.py we define a function home(request) as following:

```python
# View for home
def home(request):
    return render(request, 'home.html', {})
```
