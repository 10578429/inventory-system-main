from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request, *args, **kwargs):
    # return HttpResponse("<h1>Home Page</h1>")
    return render(request, 'home.html', {})


def contact(request, *args, **kwargs):
    return render(request, 'contact.html', {})
