from django.shortcuts import render
from django.views import generic 
from .models import Recipe


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-added_on')[0:6]
    template_name = 'index.html'

