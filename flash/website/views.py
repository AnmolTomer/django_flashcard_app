from django.shortcuts import render

# Create your views here.


# View for home
def home(request):
    return render(request, 'home.html', {})


def add(request):
    from random import randint
    num_1 = randint(0, 10)
    num_2 = randint(0, 10)

    if request.method == "POST":
        # Comes from the input box where we named it answer
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        correct_answer = int(old_num_1) + int(old_num_2)

        if(int(answer) == correct_answer):
            my_answer = "Correct! " + old_num_1 + " + " + old_num_2 + " = " + answer
        else:
            my_answer = "Incorrect! " + old_num_1 + " + " + old_num_2 + \
                " does not equals " + \
                str(answer) + ". Correct answer is: " + str(correct_answer)
        return render(request, 'add.html', {
            'answer': answer,
            'my_answer': my_answer,
            'num_1': num_1,
            'num_2': num_2
        })
        # return the page add.html and in context {} we return the key-value pair of variable answer.
    return render(request, 'add.html', {
        'num_1': num_1,
        'num_2': num_2,
    })


def subtract(request):
    from random import randint
    num_1 = randint(0, 10)
    num_2 = randint(0, 10)

    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        correct_answer = int(old_num_1) - int(old_num_2)

        if(int(answer) == correct_answer):
            my_answer = "Correct! " + old_num_1 + " - " + old_num_2 + " = " + answer
        else:
            my_answer = "Incorrect! " + old_num_1 + " - " + old_num_2 + \
                " does not equals " + \
                str(answer) + ". Correct answer is: " + str(correct_answer)

        return render(request, 'subtract.html', {
            'answer': answer,
            'my_answer': my_answer,
            'num_1': num_1,
            'num_2': num_2
        })
    return render(request, "subtract.html", {
        'num_1': num_1,
        'num_2': num_2,
    })


def multiply(request):
    from random import randint
    num_1 = randint(0, 10)
    num_2 = randint(0, 10)

    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        correct_answer = int(old_num_1)*int(old_num_2)
        if(int(answer) == correct_answer):
            my_answer = "Correct! " + old_num_1 + " * " + old_num_2 + " = " + answer
        else:
            my_answer = "Incorrect! " + old_num_1 + " * " + old_num_2 + \
                " does not equals " + \
                str(answer) + ". Correct answer is: " + str(correct_answer)
        return render(request, 'multiply.html', {
            'answer': answer,
            'my_answer': my_answer,
            'num_1': num_1,
            'num_2': num_2
        })
    return render(request, "multiply.html", {
        'num_1': num_1,
        'num_2': num_2,
    })


def divide(request):
    from random import randint
    num_1 = randint(1, 10)
    num_2 = randint(1, 10)

    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        correct_answer = int(old_num_1)/int(old_num_2)

        if(answer == correct_answer):
            my_answer = "Correct! " + old_num_1 + \
                " / " + old_num_2 + " = " + int(answer)
        else:
            my_answer = "Incorrect! " + old_num_1 + " / " + old_num_2 + \
                " does not equals " + \
                str(answer) + ". Correct answer is: " + str(correct_answer)

        return render(request, "divide.html", {
            'answer': answer,
            'my_answer': my_answer,
            'num_1': num_1,
            'num_2': num_2
        })
    return render(request, "divide.html", {
        'num_1': num_1,
        'num_2': num_2,
    })
