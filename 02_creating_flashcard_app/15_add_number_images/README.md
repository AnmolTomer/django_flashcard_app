# Adding number images as flashcards

- We will be using some basic images of numbers, you can change these up as per your design needs.

- Normally, when it comes to images we use something called a static directory, however we won't be using that here in exactly that manner.

- Go to flash >> settings.py need to add a few changes in that file as follows:

```python
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),
                    ]
```

- Inside flash directory create static>>images, nested folder.

- At the top of the page we add `{% load static %}` tag or we may also do {% static 'images/0.png' %} if we were displaying image normally.

- But that's not the case here, we want flashcards as per the random number that is generated.

- We will be using regular <img> tag in this case due to that in the following manner:

```html
<h1>
  <img src="../../static/images/{{num_1}}.png" />+<img
  src="../../static/images/{{num_2}}.png"
</h1>
```
