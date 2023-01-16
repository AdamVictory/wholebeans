from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('recipe_name',)}
    list_filter = ('status', 'added_on', 'updated_on', 'likes')
    list_display = ('recipe_name', 'added_on', 'status', 'updated_on')
    search_fields = ('recipe_name', 'description', 'ingredients', 'method')
    summernote_fields = ('description', 'ingredients', 'method')
    actions = ['approve_recipes']

