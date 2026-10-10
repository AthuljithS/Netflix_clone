from django.shortcuts import render,redirect
from django.contrib.auth import authenticate 
from .models import Movie
# Create your views here.
#login page
def login_view(request):
    error=None
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user= authenticate(request, username=username, password=password)
        if user:
            return redirect('home')
        else:
            error='Invalid username or password!'
    return render(request,'home/login.html',{'error':error})

#home page
def home_view(request):
    #fetch all records from database
    movies= Movie.objects.all()
    return render(request,'home/home.html',{'movies': movies})