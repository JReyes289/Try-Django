from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(*args, **kwargs)
    print(request)
    print(request.user)
    #return HttpResponse("<h1>Hello world</h1>") # string of html code
    return render(request,"home.html",{})

def contact_view(request, *args, **kwargs):
    return render(request,"contact.html",{}) # string of html code    

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text":"This is about us",
        "my_number":124,
        "my_list":[1,2,3,4]
    }
    return render(request,"about.html",my_context) # string of html code    

def Social_view(request, *args, **kwargs):
    return render(request,"about.html",{}) # string of html code    
