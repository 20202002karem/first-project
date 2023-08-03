from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User
    form = CustomUserChangeForm # used for update the object 
    add_form = CustomUserCreationForm # used to create an object
    list_display = ["id", "email", "username"]
    
admin.site.register(User, CustomUserAdmin)