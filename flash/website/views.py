from django.shortcuts import render

# Create your views here.


# View for home
def home(request):
    return render(request, 'home.html', {})

# --------------------------------------------------------------ADD-------------------------------------------------------------------------


def add(request):
    from random import randint
    num_1 = randint(0, 10)
    num_2 = randint(0, 10)

    if request.method == "POST":
        # Comes from the input box where we named it answer
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
# Error handling if form submitted without answer and warning displayed.
        if not answer:
            my_answer = "Hey! You forgot to fill the answer."
            color = "warning"
            return render(request, "add.html", {
                'color': color,
                'my_answer': my_answer,
                'num_1': num_1,
                'num_2': num_2,
                'answer': answer,
            })

        correct_answer = int(old_num_1) + int(old_num_2)

        if(int(answer) == correct_answer):
            my_answer = "Correct! " + old_num_1 + " + " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_answer = "Incorrect! " + old_num_1 + " + " + old_num_2 + \
                " does not equals " + \
                str(answer) + ". Correct answer is: " + str(correct_answer)
            color = "danger"
        return render(request, 'add.html', {
            'answer': answer,
            'my_answer': my_answer,
            'num_1': num_1,
            'num_2': num_2,
            'color': color,
        })
        # return the page add.html and in context {} we return the key-value pair of variable answer.
    return render(request, 'add.html', {
        'num_1': num_1,
        'num_2': num_2,
    })

# --------------------------------------------------------------SUBTRACT-------------------------------------------------------------------------


def subtract(request):
    from random import randint
    num_1 = randint(0, 10)
    num_2 = randint(0, 10)

    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
# Error handling if form submitted without answer and warning displayed.
        if not answer:
            my_answer = "Hey! You forgot to fill the answer."
            color = "warning"
            return render(request, "subtract.html", {
                'color': color,
                'my_answer': my_answer,
                'num_1': num_1,
                'num_2': num_2,
                'answer': answer,
            })

        correct_answer = int(old_num_1) - int(old_num_2)

        if(int(answer) == correct_answer):
            my_answer = "Correct! " + old_num_1 + " - " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_answer = "Incorrect! " + old_num_1 + " - " + old_num_2 + \
                " does not equals " + \
                str(answer) + ". Correct answer is: " + str(correct_answer)
            color = "danger"

        return render(request, 'subtract.html', {
            'answer': answer,
            'my_answer': my_answer,
            'num_1': num_1,
            'num_2': num_2,
            'color': color,
        })
    return render(request, "subtract.html", {
        'num_1': num_1,
        'num_2': num_2,
    })

# --------------------------------------------------------------MULTIPLY-------------------------------------------------------------------------


def multiply(request):
    from random import randint
    num_1 = randint(0, 10)
    num_2 = randint(0, 10)

    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

# Error handling if form submitted without answer and warning displayed.
        if not answer:
            my_answer = "Hey! You forgot to fill the answer."
            color = "warning"
            return render(request, "multiply.html", {
                'color': color,
                'my_answer': my_answer,
                'num_1': num_1,
                'num_2': num_2,
                'answer': answer,
            })

        correct_answer = int(old_num_1)*int(old_num_2)
        if(int(answer) == correct_answer):
            my_answer = "Correct! " + old_num_1 + " * " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_answer = "Incorrect! " + old_num_1 + " * " + old_num_2 + \
                " does not equals " + \
                str(answer) + ". Correct answer is: " + str(correct_answer)
            color = "danger"

        return render(request, 'multiply.html', {
            'answer': answer,
            'my_answer': my_answer,
            'num_1': num_1,
            'num_2': num_2,
            'color': color,

        })
    return render(request, "multiply.html", {
        'num_1': num_1,
        'num_2': num_2,
    })

# --------------------------------------------------------------DIVIDE-------------------------------------------------------------------------


def divide(request):
    from random import randint
    num_1 = randint(0, 10)
    num_2 = randint(1, 10)

    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

# Error handling if form submitted without answer and warning displayed.
        if not answer:
            my_answer = "Hey! You forgot to fill the answer."
            color = "warning"
            return render(request, "divide.html", {
                'color': color,
                'my_answer': my_answer,
                'num_1': num_1,
                'num_2': num_2,
                'answer': answer,
            })

        correct_answer = int(old_num_1)/int(old_num_2)
        correct_answer = float("{:.2f}".format(correct_answer))

        if("{:.2f}".format(float(answer)) == "{:.2f}".format(float(correct_answer))):
            my_answer = "Correct! " + old_num_1 + \
                " / " + old_num_2 + " = " + str(answer)
            color = "success"
        else:
            my_answer = "Incorrect! " + old_num_1 + " / " + old_num_2 + " does not equals " + \
                str(answer) + ". Correct answer is: " + str(correct_answer)
            color = "danger"

        return render(request, "divide.html", {
            'answer': answer,
            'my_answer': my_answer,
            'num_1': num_1,
            'num_2': num_2,
            'color': color,
        })
    return render(request, "divide.html", {
        'num_1': num_1,
        'num_2': num_2,
    })
