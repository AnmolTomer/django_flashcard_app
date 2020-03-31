from django.shortcuts import render

# Create your views here.


# View for home
def home(request):
    return render(request, 'home.html', {})


def add(request):
    if request.method == "POST":
        # Comes from the input box where we named it answer
        answer = request.POST['answer']
        return render(request, 'add.html', {'answer': answer})
        # return the page add.html and in context {} we return the key-value pair of variable answer.
    return render(request, 'add.html', {})


def subtract(request):
    if request.method == "POST":
        answer = request.POST['answer']
        return render(request, 'subtract.html', {'answer': answer})
    return render(request, "subtract.html", {})


def multiply(request):
    if request.method == "POST":
        answer = request.POST['answer']
        return render(request, 'multiply.html', {'answer': answer})
    return render(request, "multiply.html", {})


def divide(request):
    if request.method == "POST":
        answer = request.POST['answer']
        return render(request, "divide.html", {'answer': answer})
    return render(request, "divide.html", {})
