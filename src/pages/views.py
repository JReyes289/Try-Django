from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(*args, **kwargs)
    print(request)
    print(request.user)
    return HttpResponse("<h1>Hello world</h1>") # string of html code

def contact_view(request, *args, **kwargs):
    return HttpResponse("<h1>contact page</h1>") # string of html code    

def about_view(request, *args, **kwargs):
    return HttpResponse("<h1>about page</h1>") # string of html code    

def contact_view(request, *args, **kwargs):
    return HttpResponse("<h1>contact page</h1>") # string of html code        