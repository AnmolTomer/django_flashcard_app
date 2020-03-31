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

- Following is the entire code for getting the answer from user, checking the correct answer and showing the result to user:

```python
if request.method == "POST":
    # Comes from the input box where we named it answer
    answer = request.POST['answer']
    old_num_1 = request.POST['old_num_1']
    old_num_2 = request.POST['old_num_2']

    correct_answer = int(old_num_1) + int(old_num_2)

    if(int(answer) == correct_answer):
        my_answer = "Correct!"
    else:
        my_answer = "Incorrect!"
    return render(request, 'add.html', {
        'answer': answer,
        'my_answer': my_answer
        })
```

- Go to add.html and after <center> tag add the following to show the result `{{my_answer}}`
