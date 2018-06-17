from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def page(request, name):
    return render(request, 'page.html', {'name': name})
