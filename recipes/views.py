from django.http.response import HttpResponse
from django.shortcuts import render


def home(request):
    # pass
    return render(request, 'recipes/pages/home.html', context={
        'name': 'André Nunes',
    })


def about(request):
    # pass
    return HttpResponse('ABOUT')
