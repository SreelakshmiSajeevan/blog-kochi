from django.shortcuts import render, HttpResponse, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
# Create your views here.
from . models import Blog
def home(request):
    # return HttpResponse("Hello")
    blog = Blog.objects.all()

    context = {
        "blog":blog
    }
    return render(request, "home.html", context)

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")


def content(request, id):
    blog = Blog.objects.get(id=id)

    context = {
        "blog": blog
    }
    return render(request, "blogcontent.html", context)

def signup(request):
    if request.method == "POST":
        fname= request.POST.get("fname")
        email= request.POST.get("email")
        password= request.POST.get("password")
        user = User.objects.create_user(username=fname, email=email,password= password)
        user.save()

        return redirect("home")
        # print(fname, email, password)
    return render(request, "signup.html")


def login(request):
    if request.method == "POST":
        fname= request.POST.get("fname")
        email= request.POST.get("email")
        password= request.POST.get("password")
        user = authenticate(request, username=fname,email=email, password=password)
        if user is not None:
            login(request, user)
        else:
            pass

    return render(request, "login.html")


def Logout(request):
    logout(request)
    return redirect("home")
