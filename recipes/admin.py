from django.contrib import admin
from .models import Recipe, RecipeIngredient
from django.contrib.auth import get_user_model
# Register your models here.

# User = get_user_model()

# class RecipeInline(admin.StackedInline):
#     model = Recipe
#     extra = 0

# class UserAdmin(admin.ModelAdmin):
#     inlines = [RecipeInline]

# admin.site.unregister(User)
# admin.site.register(User,UserAdmin)

class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    readonly_fields =['quantity_as_float','as_mks','as_imperial']
    # fields = ['name','quantity','unit','directions']
    extra = 0

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ['name','user']
    readonly_fields = ['timestamp','updated']
    raw_id_field = ['user']

admin.site.register(Recipe,RecipeAdmin)
