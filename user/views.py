from django.shortcuts import render, get_list_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
# Create your views here.
def home(request):
    if not request.user or not request.user.is_authenticated:
        return redirect('/user/login')
    return render(request, 'home.html',)

def register_view(request):
    """
    Method type:
    POST -> read request data, and create a new user 
    GET -> redirect the user to the registration
    """
    if request.user and request.user.is_authenticated:
        return redirect('/user')
    form = CustomUserCreationForm()
    if request.method == "POST":
        # read request data
        # read request Files
        # validate the data
        print(request.FILES)
        form = CustomUserCreationForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return  redirect('/user/login')
    return render(request, 'register.html',{'form':form})

def login_view(request):
    """
    Method type:
    POST -> read request data, and login the user 
    GET -> redirect the user to the login
    """
    # if the user is login ,then redirect to home page
    if request.user and request.user.is_authenticated:
        return redirect('/user')
    
    if request.method == "POST":
        # read email and password
        # validate the data
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username = email, password = password )
        if user is not None:
            login(request, user)
            return redirect('/user/')
    return render(request, 'login.html',)


def logout_view(request):
    logout(request)
    return redirect('/user/login')
