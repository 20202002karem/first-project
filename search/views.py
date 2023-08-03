from django.shortcuts import render

from articale.models import Article
from recipes.models import Recipe

SEARCH_TYPE_MAPPING = {
    'articles': Article,
    'article': Article,
    'recipes': Recipe,
    'recipe': Recipe,
}

# Create your views here.

def search_view(request):
    query = request.GET.get('q')
    search_type = request.GET.get('type')
    klass = Recipe
    if search_type in SEARCH_TYPE_MAPPING.keys():
        klass = SEARCH_TYPE_MAPPING[search_type]
    
    qs = klass.objects.search(query=query)
    context ={
        'queryset':qs,
        'enter':False,
        
    }
    template = 'search/result-view.html'
    if request.htmx:
        context['enter']=True
        context['queryset'] = qs[:3]
        template = 'search/partials/result.html'
    return render(request,template,context=context)