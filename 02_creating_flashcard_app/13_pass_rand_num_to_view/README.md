# Pass Random Numbers to view

- So, we have our random numbers being generated, on doing reload we get new ones as well.

- Now we need to be able to submit and get result for the numbers being displayed.

- We need to pass the two generated random numbers num_1 and num_2 back to the backend again, and compare it with the answer received from the form.

- To do so we need to create some hidden fields on the form.

- After creating two hidden input in add.html and other math pages we need to enter values into them and do some logic processing as follows:

```html
<input type="hidden" name="old_num_1" value="{{num_1}}" />
<input type="hidden" name="old_num_2" value="{{num_2}}" />
```

- On adding the code above, upon viewing the page source we will be able to see generated random numbers in page source.

-
