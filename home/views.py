from django.shortcuts import render


def index(request):
    return render(request, 'home.html')


def newsletter(request):
    return render(request, 'newsletter.html')
