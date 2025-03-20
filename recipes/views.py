from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # This app's name ('recipes'), specified in the RecipesConfig class,
    # defined in recipes.apps, must be added to the INSTALLED_APPS list in
    # projeto.settings in order for Django to look for the template file
    # ('home.html') inside the recipes directory.
    return render(request, 'recipes/home.html',
                  context={'name': 'Henrique de Oliveira'})


def contact(request):
    return HttpResponse('Contact info')
