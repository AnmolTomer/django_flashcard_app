# Creating math urls

- We can go to **base.html** and edit the links for add, subtract etc. in the following manner:

```html
<a class="nav-link" href="./add.html">Add</a>
```

- Alternatively, there is a better way that we may use that is Django links, using an url tag and it creates these links immediately.

- To create django links we use django templating language tags {% %}, between these tags we define {% url 'add' %} 'add' is the name='add' attribute that we gave in the urls.py file.

- We reference the links using just by referencing those names that we put in urls.py file.

- `Why is this important ?` Glad you asked, say you have website with 100s, or even 1000s of pages and have links scattered all over the place, in that case we might not want to go through all the links and change those everytime we want to make some changes we have to change .html links everywhere.

- Also if you don't want to go to add.html instead we just want `localhost:8000/add` to point to add, in that case in urls.py file we just change add.html to add it will still work. Noicee right! 😎
