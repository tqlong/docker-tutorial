from django.shortcuts import render


def index(request):
    context = dict(
        name='Long'
    )
    return render(request, 'index.html', context=context)
