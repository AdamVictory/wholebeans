from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View 
from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib import messages 
from django.db.models import Q 
from .models import Recipe
from .forms import CommentForm, RecipeForm, ApproveForm
from django.urls import reverse_lazy


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-added_on')[0:6]
    template_name = 'index.html'


class AllRecipes(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('recipe_name')
    template_name = 'all_recipes.html'
    paginate_by = 6


class RecipeView(View):
    def get(self, request, slug, *args, **kwargs): 
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('added_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request, 
            "recipe_view.html", 
            {
                "recipe": recipe,
                "comments": comments, 
                "commented": False, 
                "liked": liked, 
                "comment_form": CommentForm()
            }
        )
    
    def post(self, request, slug, *args, **kwargs): 
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('added_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists(): 
            liked = True 
        
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username 
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request, 
            "recipe_view.html", 
            {
                "recipe": recipe, 
                "comments": comments, 
                "commented": True, 
                "liked": liked, 
                "commented_form": CommentForm()
            }
        )


class ModerateRecipeView(View): 

    def get(self, request, slug, *args, **kwargs): 
        queryset = Recipe.objects.filter(status=0)
        recipe = get_object_or_404(queryset, slug=slug)

        return render(
            request, 
            "moderate_recipe_view.html", 
            {
                "recipe": recipe, 
            }
        )


class RecipeLike(View):

    def post(self, request, slug): 
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists(): 
            recipe.likes.remove(request.user)
        else: 
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_view', args=[slug]))


class AddRecipe(View): 

    def get(self, request): 
        context = {'form': RecipeForm()}
        return render(request, 'add_recipe.html', context)
    
    def post(self, request, *args, **kwargs): 

        form = RecipeForm(request.POST, request.FILES)
        title = form.instance.recipe_name
        recipe_exists = Recipe.objects.filter(
            Q(recipe_name__iexact=title)
        ).exists()
        if recipe_exists: 
            messages.error(
                request, 
                'Recipe name exists, please choose another name'
            )
            context = {'form': form}
            return render(request, 'add_recipe.html', context)
        if form.is_valid():
            form.instance.author = self.request.user 
            try: 
                form.save()
                messages.success(request, "Your recipe is awaiting approval")
                return redirect('home')
            except: 
                messages.error(request, 
                               'Error: Only images can be uploaded.'
                               'Retry')
                context = {'form': form}
                return render(request, 'add_recipe.html', context)
        else: 
            messages.error(request, 
                           'Error: The form is invalid, '
                           'please retry')
            context = {'form': form}
            return render(request, 'add_recipe.html', context)


class UserRecipe(generic.ListView): 
    template_name = 'user_recipes.html'
    model = Recipe
    context_object_name = 'recipes'
    paginate_by = 6 

    def get_queryset(self): 
        return Recipe.objects.filter(
            author=self.request.user, status=1
        ).order_by('-added_on')


class UpdateRecipe(UpdateView):
    model = Recipe 
    template_name = 'update_recipe.html'
    form_class = RecipeForm
    success_url = reverse_lazy('user_recipes')


class ModerateUpdateRecipe(UpdateView): 
    model = Recipe
    template_name = 'update_recipe.html'
    success_url = reverse_lazy('moderate_recipes')

class DeleteRecipe(DeleteView): 
    model = Recipe
    template_name = 'delete_recipe.html'
    success_url = reverse_lazy('moderate_recipes')

class ModerateDeleteRecipe(UpdateView): 
    model = Recipe
    template_name = 'delete_recipe.html'
    success_url = reverse_lazy('moderate_recipes')

class ApproveRecipe(UpdateView): 
    model = Recipe
    template_name = 'approve_recipe.html'
    form_class = ApproveForm
    success_url = reverse_lazy('moderate_recipes')



def search_results(request): 

    if request.method == "GET": 
        searched = request.GET['searched']
        recipes = Recipe.objects.distinct(). filter( 
            Q(recipe_name__icontains=searched) |
            Q(description__icontains=searched) |
            Q(ingredients__icontains=searched) 
        )
        return render(request, 'search_results.html', 
                      {'searched': searched, 'recipes': recipes}) 
    else: 
        return render(request, 'search_results.html', {})


class ModerateRecipes(generic.ListView): 
    template_name = 'moderate_recipes.html'
    model = Recipe
    context_object_name = 'recipes'
    paginate_by = 6

    def get_queryset(self): 
        return Recipe.objects.filter(
             status=0
        ).order_by('-added_on')
        




        

