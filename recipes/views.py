from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from django.http import HttpResponse, Http404
from django.urls import reverse
from .models import Recipe, RecipeIngredient
from .forms import RecipeForm, RecipeIngredientForm
# Create your views here.
@login_required
def recipe_list_view(request):
    qs = Recipe.objects.filter(user= request.user)
    context={
        'object_list': qs,
    }
    return render(request, 'recipes/list.html', context=context)

@login_required
def recipe_detail_view(request,id=None):
    hx_url = reverse('recipes:hx_detail', kwargs={'id': id})
    context={
        'hx_url':hx_url,
    }
    return render(request, 'recipes/detail.html', context=context)

@login_required
def recipe_detail_hx_view(request, id=None):
    try:
        obj = Recipe.objects.get(id=id,user=request.user)
    except:
        obj = None
    if obj is None:
        return HttpResponse('Not found')
    context = {
        'object':obj,
    }
    return render(request, 'recipes/partials/detail.html', context=context)


@login_required
def recipe_create_view(request):
    form = RecipeForm(request.POST or None)
    context={
        'form':form,
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        if request.htmx:
            headers ={
                'HX-Redirect': obj.get_absolute_url(),
            }
            return HttpResponse('Created',headers=headers)
    return render(request, 'recipes/create-update.html', context=context)

@login_required
def recipe_ingredient_update_hx_view(request, id_parent=None, id=None):
    if not request.htmx:
        raise Http404
    try:
        parent_obj = Recipe.objects.get(id=id_parent, user=request.user)
    except:
        parent_obj = None
    if parent_obj is None:
        return HttpResponse('Not found')
    instance = None
    if id is not None:
        try:
            instance = RecipeIngredient.objects.get(id=id, recipe=parent_obj)
        except:
            instance = None
    form = RecipeIngredientForm(request.POST or None, instance=instance)
    url = reverse('recipes:hx_ingredient_create', kwargs={'id_parent': id_parent})
    if instance:
        url = instance.get_hx_edit_url()
    context = {
        'form': form,
        'url': url,
        'object': instance,
    }
    if form.is_valid():
        new_obj = form.save(commit=False)
        if instance is None:
            new_obj.recipe = parent_obj
        new_obj.save()
        context['object']= new_obj
        return render(request, 'recipes/partials/ingredient-inline.html', context=context)
    return render(request,'recipes/partials/ingredient-form.html', context= context)


@login_required
def recipe_update_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user= request.user)
    form = RecipeForm(request.POST or None , instance=obj)
    new_ingredient_url = reverse('recipes:hx_ingredient_create',kwargs={'id_parent':obj.id})
    context= {
        'form': form,
        'obj':obj,
        'new_ingredient_url':new_ingredient_url,
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        context['masege']='Data saved'
        if request.htmx:
            return render(request, 'recipes/partials/forms.html', context)
    return render(request, 'recipes/create-update.html', context= context)

    # RecipeIngredientFormset = modelformset_factory(RecipeIngredient, form=RecipeIngredientForm,extra=0)
    # qs = obj.recipeingredient_set.all()
    # formset = RecipeIngredientFormset(request.POST or None, queryset=qs )


@login_required
def recipe_delete_view(request,id=None):
    try:
        obj = Recipe.objects.get(id=id,user=request.user)
    except:
        obj = None
        if obj is None:
            return HttpResponse('Not Found')
        raise Http404
    if request.method == 'POST':
        obj.delete()
        success_url = reverse('recipes:list')
        if request.htmx:
            headers={
                'HX-Redirect': success_url,
            }
            return HttpResponse('success',headers=headers)
        return redirect(success_url)
    context={
        'object':obj,
    }
    return render(request,'recipes/delete.html',context=context)

@login_required
def recipe_ingredient_delete_view(request,id_perant=None,id=None ):
    try:
        obj = RecipeIngredient.objects.get(id=id,
            recipe__id=id_perant,recipe__user=request.user)
    except:
        obj= None
        if request.htmx:
            return HttpResponse('Not Found')
        raise Http404
    if request.method == 'POST':
        obj.delete()
        success_url = reverse('recipes:detail',kwargs={'id':id_perant})
        if request.htmx:
            headers={
                'HX_REdirect': success_url,
            }
            return render(request, 'recipes/partials/inredient-inline-delete-respeonse.html',
                            context=context)
        return redirect(success_url)
    context={
        'object':obj,
    }
    return render(request, 'recipes/delete.html',context=context)
        





















