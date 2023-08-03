from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    
    class Meta:
        db_table = "Authors"
    
    def __str__(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None) #author_id
    name = models.CharField(max_length=255) # name, title, email,
    num_of_pages = models.IntegerField(default=1)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "books"
    
    def __str__(self):
        return self.name
    
    
# 1 Create The Model
# 2 Create Migration for that modle
    # python manage.py makemigrations
# 3 Reflect migration to the database
    # python manage.py migration

# table name = app name +_+ model name


# Operationns on Models CRUD
    # create:
# author1 = Author.objects.create(
#     name ="Ahmad",
#     bio = ""
# ) #id = 1
# book1 =Book.objects.create(
#     author_id = 3,
#     # author = author1,
#     name = "Book #1",
#     num_of_pages = 10,
#     content = "Content of Book #3"
    
# )
#     # List (Get) -> return multpil objecte
# books = Book.objects.all() # list all objects
# Book.objects.count() #count all objects

#     # Retrieve (Get) -> return singele objecte
# Book.objects.all()[0] # return the first objects
# Book.objects.all().first() # return the first objects
# Book.objects.all().last() # return the last objects
# Book.objects.all().get(id=7) # return the specified object, else throw Excepthin

#     # Update an object 
# book = Book.objects.get(id = 7)
# book.num_of_pages = 20
# book.content =book.content + " new. "
# book.save() # to save changes in the database

#     # Delete an object 
# book = Book.objects.get(id = 3)
# book.delete()





# Filter -> return multpil objectes
Book.objects.filter()

# >  __gt  Eg: Book.objects.filter(num_of_pages__gt=10)
# <  __lt  Eg: Book.objects.filter(num_of_pages__lt=10)
# >=  __gte  Eg: Book.objects.filter(num_of_pages__gte=10)
# <=  __lte  Eg: Book.objects.filter(num_of_pages__lte=10)

# check if string contains:   __contains , __icontains
    # __contains : search with case-sensitive       Eg:Book.objects.filter(name__contains="book")
    # __icontains : search without case-sensitive  Eg:Book.objects.filter(name__icontains="book")

# check is is null
    # isnull Eg: Book.objects.filter(name__isnull=True)
    





# Order 
    # Book.objects.all().order_by('created_at)  Asc order
    # Book.objects.all().order_by('-created_at)  Dsc order
    




