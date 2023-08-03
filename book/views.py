from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from book.models import Book   # .models
# Create your views here.
def first(request):
    return HttpResponse("<h1>this is the first Book<h1>")

def home(request):
    colors = ["red","green","Blue"]
    return render(request,"home.html",{"name":"APreheem", "age":"20","colors":colors})

def all(request):
    books = Book.objects.all().order_by('-created_at')
    return render(request,'books_List.html',{'books':books} )

def get(request, id ):
    book = get_object_or_404(Book, id= id)
    return  render(request, 'book.html',{"book":book})
    # try:
    #     book = Book.objects.get(id=id)
    #     return  render(request, 'book.html',{"book":book})
    # except:
    #     return  HttpResponse("Dose Not Exist")
    












## Create anew App 
# 1- run -> python manage.py startapp <app_name>
# 2- register the new app in the 'INSTAALLED_APPS'
# 3- create 'urls.py' module
# 4- create our 'view' functions
# 5- Link route to the view
# 5- Create a 'templete' html file