from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from django.http import Http404
from django.db.models import Q
# Create your views here.
def articale_detail_view(request,slug=None):
    articale_obj = None
    if slug is not None:
        try:
            articale_obj = Article.objects.get(slug=slug)
        except Article.DoesNotEXist:
            raise Http404
        except Article.MultipleObjectsReturned:
            article_obj = Article.objects.filter(slug=slug).first()
        except:
            raise Http404
    context = {
        'obj': articale_obj, 
    }
    return render(request, 'articale/detail.html', context=context)


def articale_search(request):
    qs = Article.objects.all()
    query = request.GET.get('q')
    qs = Article.objects.search(query)
    context ={
        'qs': qs,
    }
    return render(request,'articale/search.html',context)

@login_required
def articale_created(request):
    form = ArticleForm(request.POST or None)
    context ={'form':form}
    if form.is_valid():
        obj = form.save()
        return redirect(obj.get_absolute_url())
        context['obj']= obj
        context['create']= True
    return render(request,'articale/created.html',context=context)
    
    
    
    
    
    
    
    
    
    
    
    # form = ArticleFormOld(request.POST or None)
    # context={
    #     "form":form
    # }
    # print(form.is_valid())
    # if form.is_valid():
    #     title = form.cleaned_data.get('title')
    #     content = form.cleaned_data.get('content')
    #     obj = Article.objects.create(title=title,content= content)
    #     context['obj']=obj
    #     context['create']=True
    # return render(request,'articale/created.html',context=context)






















