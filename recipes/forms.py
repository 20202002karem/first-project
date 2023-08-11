from django import forms
from .models import Recipe,RecipeIngredient, RecipeIngredientImage


class RecipeIngredientImageForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredientImage
        fields = ['image']

class RecipeForm(forms.ModelForm):
    required_css_class = 'required_field'
    error_css_class = 'error_field'
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'directions']
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'eee'
        self.fields['name'].widget.attrs.update({'class': 'form-control-2'}, help_text='adsfdfe')
        self.fields['description'].widget.attrs.update({'row':'2'})
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': f'Recipe-{field}',
                
                })

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['name', 'quantity', 'unit']