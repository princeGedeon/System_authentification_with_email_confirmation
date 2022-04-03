from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def hello(request):
    return render(request, "app/index.html")

def register(request):
    if request.method=="POST":
        #Recupérer les données entrés par user
        username=request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if User.objects.filter(username=username):
            messages.error(request,"Ce nom a été déja pris")
            return redirect("register")
        if User.objects.filter(email=email):
            messages.error(request, "Cet email a été déja prise")
            return redirect("register")
        if not username.isalnum():
            messages.error(request,"Le nom doit etre alpha numérique")
            return redirect("register")
        if password!=password2:
            messages.error(request,"Les deux mots de passes ne correspondent pas")
            return redirect("register")
        new_user=User.objects.create_user(username,email,password)
        new_user.first_name=name
        new_user.save()
        messages.success(request,"Votre compte a été créé avec succes")

        return redirect('login')



    return render(request,"app/register.html")

def loginView(request):
    if request.method=="POST":
        #Recupérer les données entrés par user
        username=request.POST['username']
        password = request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            firstname=user.first_name
            messages.success(request,'Vous etes connectés')
            return redirect('home')
        else:
            messages.error(request,'Mauvaise authentification')
            return redirect("login")
    return render(request,'app/login.html')
def logoutView(request):
    logout(request)
    messages.success(request,"Vous avez ete bien deconnecte")
    return redirect("home")