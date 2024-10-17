from django import forms
from .models import Recipe

class Recipeform(forms.ModelForm):
    class Meta:
        model= Recipe
        fields= ['title', 'description', 'ingredients', 'instructions']

