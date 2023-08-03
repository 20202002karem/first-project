from django.db import models
from django.conf import settings
from django.urls import reverse
from django.db.models import Q 
from .validators import validat_unit_of_measure
from .utils import number_str_to_float
import pint
# Create your models here.

User = settings.AUTH_USER_MODEL

class RecipeQuerySet(models.QuerySet):
    def search(self, query):
        if query is None or query == "":
            return self.none()
        lookup =(   Q(name__icontains=query) |
                    Q(description__icontains=query)|
                    Q(directions__icontains=query))
        return self.filter(lookup)

class RecipeManager(models.Manager):
    def get_queryset(self):
        return RecipeQuerySet(self.model, using=self._db)
    def search(self, query):
        return self.get_queryset().search(query)

class Recipe(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE )
    name = models.CharField(max_length=220)
    description = models.TextField(null=True, blank=True)
    directions = models.TextField(null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    objects = RecipeManager()
    
    def get_absolute_url(self):
        return reverse('recipes:detail', kwargs={'id':self.id})
    
    def get_hx_url(self):
        return reverse('recipes:hx_detail', kwargs={'id':self.id})
    
    def get_ingredients_children(self):
        return self.recipeingredient_set.all()
    
    def get_delete_url(self):
        return reverse('recipes:delete', kwargs={'id': self.id })


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(null=True,blank=True)
    quantity = models.CharField(max_length=50)
    quantity_as_float = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=50,validators=[validat_unit_of_measure])
    directions = models.TextField(null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def get_absolute_url(self):
        return self.recipe.get_absolute_url()
    
    def get_hx_edit_url(self):
        kwargs={
            'id_parent': self.recipe.id,
            'id': self.id,
        }
        return reverse('recipes:hx_ingredient_detail', kwargs=kwargs)
    
    def get_delete_url(self):
        kwargs= {
            'id_perant': self.recipe.id,
            'id': self.id,
        }
        return reverse('recipes:ingredient_delete', kwargs=kwargs)
    
    def convert_to_system(self, system='mks'):
        if self.quantity_as_float is None:
            return None
        ureg = pint.UnitRegistry(system=system)
        measurement = self.quantity_as_float * ureg[self.unit]
        return measurement
    
    def as_mks(self):  # meters kilogram seconde
        measurement = self.convert_to_system(system='mks')
        return measurement.to_base_units()
    
    def as_imperial(self):  # miles pound seconde
        measurment = self.convert_to_system(system='imperial')
        return measurment.to_base_units()
    
    def save(self, *args, **kwargs):
        qty = self.quantity
        qty_as_float , qty_as_float_success = number_str_to_float(qty)
        if qty_as_float_success:
            self.quantity_as_float = qty_as_float
        else:
            self.quantity_as_float = None
        super().save(*args, **kwargs)
    
    
    
    
    
    
    