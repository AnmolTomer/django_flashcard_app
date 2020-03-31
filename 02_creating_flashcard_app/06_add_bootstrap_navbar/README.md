# Adding a bootstrap navigation bar

- Go to this [link](https://getbootstrap.com/docs/4.4/components/navbar/) on BootStrap page to get starter navigation bar code.

- Go to base.html and right below body tag paste the starter navbar code you copied. As we want navbar on everypage, so we are pasting in base.html.

- Hello World on home page is right against the page to fix this what we do is add a new div after </nav>

```html
<br />
<div class="container">
  {% block 'content' %}
  <!--  -->
  {% endblock %}
</div>
```

- To change the navbar from light to dark do the following changes:

```html
<nav class="navbar navbar-expand-lg navbar-light bg-light"></nav>
<!-- Change the above to dark-->
<nav class="navbar navbar-expand-lg navbar-dark bg-dark"></nav>
```

- Change Navbar ins starter code to Math Flashcards and remove the Search box from navbar, remove the disabled as well as dropdown.

- Create 4 pages for addition, subtraction, multiplication and division.

- Now you will end up with a navbar and we are headed in the right direction. It's that easy to use bootstrap, you just copy, paste the component and after that modify it as per requirement.
