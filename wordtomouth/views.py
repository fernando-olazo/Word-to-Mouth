from django.shortcuts import redirect, render
from login_app.models import User
from .models import *

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')

    context = {
        'this_user': User.objects.get(id=request.session['user_id']),
        'all_recipes': Recipe.objects.all(), #if I want all messages
    }
    return render(request, 'recipes.html',context)



def create_recipe(request):
    if request.method != 'POST' or 'user_id' not in request.session:
        return redirect('/')
    #specify the user
    this_user= User.objects.filter(id=request.session['user_id'])[0]

    #create the new message
    new_recipe= Recipe.objects.create(
        r_title= request.POST['r_title'],
        ingredients= request.POST['ingredients'],
        preparation= request.POST['preparation'],
        posted_by= this_user #it tells you that is logged in posted something

    )
    return redirect('/recipes')

def delete_recipe(request, recipe_id):
    if request.method != 'POST' or 'user_id' not in request.session:
        return redirect('/')
    #specify the message
    this_recipe= Recipe.objects.get(id=recipe_id)
    #delete
    this_recipe.delete()
    return redirect('/recipes')
