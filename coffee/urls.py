from django.urls import path 
from . import views 


urlpatterns = [ 
    path('', views.RecipeList.as_view(), name='home'), 
    path('recipes/all_recipes', views.AllRecipes.as_view(), name='all_recipes'), 
    path('recipes/<slug:slug>/', views.RecipeView.as_view(), name='recipe_view'), 
    path('recipes/<slug:slug>/moderate_recipe_view', views.ModerateRecipeView.as_view(), name='moderate_recipe_view'), 
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'), 
    path('recipes/add', views.AddRecipe.as_view(), name='add_recipe'), 
    path('recipes/my_recipes', views.UserRecipe.as_view(), name='user_recipe'), 
    path('recipes/update_recipe/<slug:slug>', views.UpdateRecipe.as_view(), name='update_recipe'), 
    path('recipes/<slug:slug>/delete_recipe/', views.DeleteRecipe.as_view(), name='delete_recipe'), 
    path('search_results', views.search_results, name='search_results'), 
    path('recipes/moderate_recipes', views.ModerateRecipes.as_view(), name='moderate_recipes'), 
    path('recipes/<slug:slug>/approve_recipe', views.ApproveRecipe.as_view(), name='approve_recipe'), 
    path('recipes/admin_update_recipe/<slug:slug>', views.ModerateUpdateRecipe.as_view(), name='moderate_delete_recipe'), 
]