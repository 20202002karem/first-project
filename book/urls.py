from django.urls import path
from .views import first,home ,all,get



urlpatterns = [
    path("first/",first),
    path("home/",home),
    path("<int:id>/",get),
    path("", all)
    
]