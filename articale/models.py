from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import slugify_instance_title
from django.urls import reverse
from django.db.models import Q
# Create your models here.

class ArticleQuerySet(models.QuerySet):
    def search(self, query):
        if query is None or query == "":
            return self.none()
        lookup = Q(name__icontains=query) | Q(content__icontains=query)
        return self.filter(lookup)

class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)
    def search(self, query):
        return self.get_queryset().search(query)
        

class Article(models.Model):
    name = models.TextField()
    content = models.TextField(default=None)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)
    description = models.TextField()
    slug = models.SlugField(unique=True, null=True,blank=True)
    
    objects = ArticleManager() 
    
    def get_absolute_url(self):
        return reverse('articale-detail', kwargs={ "slug": self.slug })
    
    def save(self,*args, **kwargs):
    #     # if self.slug is not None:
        if self.slug is None:
            obj = slugify_instance_title(self)
            self.slug = obj.slug
        super().save(*args,**kwargs)



def article_pre_save(sender,instance,*arge,**kwarge):
    if instance.slug is None:
        pre_slug = slugify_instance_title(instance,save= False)
pre_save.connect(article_pre_save,sender=Article)

def article_post_save(created,instance,*args,**kwargs):
    if created:
        slugify_instance_title(instance,save= True)

post_save.connect(article_post_save,sender=Article)