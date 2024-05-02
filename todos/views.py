from django.shortcuts import render
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
