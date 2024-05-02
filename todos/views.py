from django.shortcuts import render
from .models import Todo


def index(request):
    context = dict(
        todos=Todo.objects.all()
    )
    return render(request, 'index.html', context=context)
