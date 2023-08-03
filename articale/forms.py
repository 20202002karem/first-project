from django import forms
from articale.models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name','content']
    
    def clean_title(self):
        cleaned_data= self.cleaned_data
        name = cleaned_data.get('name')
        if name.lower().strip() == "qaz":
            # raise forms.ValidationError("this title is taken")
            self.add_error("title","this title is taken")
        return name
    
    def clean(self):
        cleaned_data = self.cleaned_data
        content = cleaned_data.get('content')
        qs = Article.objects.filter(content__icontains=content)
        if qs.exists():
            raise forms.ValidationError("this title is taken")
        return cleaned_data
    
