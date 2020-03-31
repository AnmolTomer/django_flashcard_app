# Form Action

- So we have our form now initialized on all four math web pages, but it is not doing anything currently. Let's change that.

- Next thing we might wanna do is create a CSRF (Cross site request forgery) token.

- It is just a token that Django will create for each web form so that hackers can't mess up with forms and send without validation of some sort.

- To create one in Django we just type in `{% csrf_token %}` after <form> tag.

- If you go to page source and see form section you will see type = hidden and some csrftoken with a long key in page source after <form> tag as follows:

```html
<form>
  <input
    type="hidden"
    name="csrfmiddlewaretoken"
    value="YMtGknYEghZBwYRh3Tw27c61jpASeUQydeVNjx4VLH4aEe00cvZ6di5NBuzSzbYs"
  />
  <div class="form-group">
    <input
      type="text"
      class="form-control"
      placeholder="Type Your Answer Here"
    />
  </div>
  <br />
  <button type="submit" class="btn btn-secondary">Submit</button>
</form>
```

---

`**What's CSRF?**`

- **Ans:** `A CSRF token is a unique, secret, unpredictable value that is generated by the server-side application and transmitted to the client in such a way that it is included in a subsequent HTTP request made by the client. When the later request is made, the server-side application validates that the request includes the expected token and rejects the request if the token is missing or invalid.

CSRF tokens can prevent CSRF attacks by making it impossible for an attacker to construct a fully valid HTTP request suitable for feeding to a victim user. Since the attacker cannot determine or predict the value of a user's CSRF token, they cannot construct a request with all the parameters that are necessary for the application to honor the request.`

### More on CSRF tokens [here](https://portswigger.net/web-security/csrf/tokens)

### More on CSRF attack [here](https://portswigger.net/web-security/csrf)

---

- After we are done with CSRF we need our form to point somewhere. Right now it is not pointing anywhere.

- So we give an action and a method to form. Method will be post. Generally options are `POST or GET`. When someone comes to the website they are getting the data.

- When user submits the data through form they are posting the form so we use `method = "POST"`, we may use method = "GET" but forms do not do that anymore so ignore GET and do POST.

- **Action**: When someone clicks, where do we want them to go, what action we want to take? Let's send the form right back to the add page i.e. itself.

- We are sending it to itself so that we may run some logic to check if the flashcard answer was answered correctly or not, and show something.

- We also want to come to the <input> section and we want to keep name to the input of the form we call it `name = "answer"`

- We give this name so that when someone submits the form, it gets passed to backend and we can reference the answer to pull the answer.

- Once this info is posted via form we haven't done anything with it in the backend, more on this in the next section.