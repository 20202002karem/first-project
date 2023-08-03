from django.urls import path
from . import views

# /user/ > home
# /user/register >register page
# /user/login > login page
# /user/logout > logout, redirect to login page

urlpatterns = [
    path('', views.home,),
    path('register', views.register_view),
    path('login', views.login_view),
    path('logout', views.logout_view),
]
