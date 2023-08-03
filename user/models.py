from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class User(AbstractUser):
    email = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=244, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='user/', null=True, default=None) # /media/users/
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = "email" 
    REQUIRED_FIELDS = ["username"]  #required in registration process 
    
    def Meta():
        db_table = "users"
    
    def __str__(self):
        return self.email  
    

# Add Image
# /media
# pip install pillow
