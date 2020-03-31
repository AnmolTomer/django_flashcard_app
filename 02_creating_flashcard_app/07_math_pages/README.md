# Creating math web pages

- Back to the three step process for creation of web page in Django : 1. Template (html), 2. View, 3. URL

- Go to templates directory and create add.html and other 3 files as well.

- Go to urls.py to create urls for all the 4 created new html files.

- In views.py add the following:

```python
def add(request):
    return render(request, 'add.html', {})


def subtract(request):
    return render(request, "subtract.html", {})


def multiply(request):
    return render(request, "multiply.html", {})


def divide(request):
    return render(request, "divide.html", {})
```
