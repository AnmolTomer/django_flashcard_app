# Form Processing

- So form is working but we aren't actually doing something on it.

- Let's change that! Go to views.py file and in the add function anything that happens logically on the add page needs to be change there. So we will change it up as needed.

- Remember when we go to the page we are getting the page, when we are submitting the form we are posting the data as follows:

```python
if request.method == "POST":
        answer = request.POST['answer']
        # Comes from the input box where we named it answer
```

- Now what we have received from the POST request we will return it to the page using the following line, where {} is the context dictionary used to return stuff from backend to frontend.

```python
return render(request, 'add.html',{'answer':answer}) # return the page add.html and in context {} we return the key-value pair of variable answer.
```

- Next we go to the add.html underneath the `<h1>Add</h1>` tag and we can directly output to the screen using `{{ answer }}` that's right. It's as simple as that.

- Works on add.html, what we are doing above in a nutshell is get something named answer if it's coming via POST request and it goes to backend and is returned to frontend.

- If someone is posting the form, take whatever they are posting, assign it to the variable, pass this variable back to the page itself and do something with it, else just return the page.
