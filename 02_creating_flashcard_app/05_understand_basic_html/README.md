# Understanding Base.html

- All the websites on the internet are almost similar, all of the websites have a navbar, some stuff (info in the middle)
  some stuff at the bottom.

- So instead of having the code for navbar and footer on every single page what we should do is break that off into its own file and write it.

- For example in navbar you client wanted a small change from Contact to Contact Us instead of doing change in every page that has navbar code we can set it up such that all the pages
  reference a single navbar file instead of having similar but repetitive navbar code on all html files and we change the code of navbar being referred once and it will change for all.

- Here we will have a navbar and we want navbar code in its own file, and we will reference it.

- Django has something called base.html file, the name base isn't strictly has to be base only you can call it what you want, conventionally it was called base.html and that convention stuck.

- Inside **base.html** we need to add a few tags and above these tags we will have stuff that we want to appear on every page of our website. Tags are:

```html
{% block 'content' %} {% endblock %}
```

- Take the part from <html> till <body> and **move** it to base.html as well as the script part of the home.html.

- At the end of the above process home.html will only have

```html
<h1>Hello, Home!- Made During COVID-19 Quarantine!</h1>
```

- Next, copy the blocks {% block 'content' %} <place your content between these>{% endblock %} on home.html page.

- At the top of home.html we will need to use another tag `{% extends 'base.html' %}`
