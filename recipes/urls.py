from django.urls import path
from .views import (
    recipe_list_view,
    recipe_create_view,
    recipe_update_view,
    
    recipe_ingredient_update_hx_view,
    recipe_detail_hx_view,
    
    recipe_delete_view,
    recipe_ingredient_delete_view,
    recipe_detail_view,
)
app_name = 'recipes'
urlpatterns = [
    path('', recipe_list_view, name='list'),
    path('create/', recipe_create_view, name='create'),
    path('<int:id>/update/',recipe_update_view, name='update'),
    
    path('hx/<int:id_parent>/ingredient/<int:id>/',
        recipe_ingredient_update_hx_view,name='hx_ingredient_detail'),
    path('hx/<int:id_parent>/ingredient/',
        recipe_ingredient_update_hx_view,name='hx_ingredient_create'),
    path('hx/<int:id>/',recipe_detail_hx_view,name='hx_detail'),
    
    path('<int:id>/delete/', recipe_delete_view, name='delete' ),
    path('<int:id_perant>/ingredient/<int:id>/delete/',
        recipe_ingredient_delete_view,name='ingredient_delete'),
    path('<int:id>/',recipe_detail_view, name='detail'),
    
]
    






