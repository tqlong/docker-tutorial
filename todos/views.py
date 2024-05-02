from django.shortcuts import render, redirect
from .models import Todo


def index(request):
    context = dict(
        todos=Todo.objects.all()
    )
    return render(request, 'index.html', context=context)


def details(request, id):
    context = dict(
        todo=Todo.objects.get(id=id)
    )
    return render(request, 'details.html', context=context)


def add(request):
    if request.method == "POST":
        todo = Todo(
            title=request.POST['title'],
            text=request.POST['text']
        )
        todo.save()
        return redirect('/todos')
    else:
        return render(request, 'add.html')
