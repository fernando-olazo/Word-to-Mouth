from django.shortcuts import redirect, render
from .models import User, UserManager
from wordtomouth.models import Recipe
import bcrypt
from django.contrib import messages

def index (request):
    request.session.flush()
    return render(request, 'login_page.html')

def user_recipes(request, poster_id):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.filter(id = request.session['user_id'])
    this_poster = User.objects.filter(id = poster_id)[0]
    context = {
        'user': this_poster,
        'all_recipes': this_poster.messages.all(),

    }
    return render(request, 'user_recipes.html', context)

def register(request): #POST
    if request.method == "POST":
        errors = User.objects.registration_validator(request.POST)
        if len(errors) != 0:
            for value in errors.values():
                messages.error(request, value)
            return redirect('/')
        hash_pw= bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        
        new_user= User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = hash_pw
        )
        
        request.session['user_id'] = new_user.id
        return redirect('/recipes')
    
    return redirect('/')

def login(request): #POST
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors) != 0:
            for value in errors.values():
                messages.error(request, value)
            return redirect('/')
        this_user = User.objects.filter(email=request.POST['email'])
        request.session['user_id'] = this_user[0].id
        return redirect('/recipes')
    
    return('/')

def edit(request, recipe_id):
    this_recipe = Recipe.objects.get(id = recipe_id)
    context = {
        'edit_recipe' : this_recipe
    }
    return render(request, "edit.html", context)

def update(request, recipe_id):
    if request.method == "POST":
        update_recipe = Recipe.objects.get(id = recipe_id)
        update_recipe.r_title = request.POST['r_title']
        update_recipe.ingredients = request.POST['ingredients']
        update_recipe.preparation = request.POST['preparation']
        update_recipe.save()
        
        return redirect('/recipes')
    
    return redirect('/')


def logout(request):
    request.session.flush()
    return redirect('/')