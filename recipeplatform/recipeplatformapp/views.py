from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseForbidden
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Recipe
from .forms import Recipeform

# Create your views here.
def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def signup(request):
    uform= UserCreationForm(request.POST)
    if request.method == "POST":
        if uform.is_valid():
            uname= uform.cleaned_data.get('username')
            pwd= uform.cleaned_data.get('password1')
            user1=User.objects.create_user(username=uname,password=pwd)
            user1.save()
            user= authenticate(request,username=uname,password=pwd)
            login(request,user)
            return redirect('home')
    else:
        form1=UserCreationForm()
        return render(request,'sign_up.html',{'form': form1})
    return render(request,'sign_up.html',{'form': uform})


def loginview(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        
        if uname and pwd:
            user = authenticate(request, username=uname, password=pwd)
            if user is not None:
                login(request, user)
                return redirect('userpage')
            else:
                message = {"error": "Invalid username or password"}
                return render(request, "login.html", message)
        else:
            message = {"error": "Please enter both username and password"}
            return render(request, "login.html", message)
    else:
        return render(request, "login.html")

def user_page(request):
    recipes = Recipe.objects.all()  
    return render(request, 'user_page.html', {'recipes': recipes})


def recipe_create(request):
    if request.method == 'POST':
        form = Recipeform(request.POST)
        if form.is_valid():
            recipe= form.save(commit=False)
            recipe.created_by = request.user
            recipe.save()
            return redirect('userpage')  
    else:
        form = Recipeform()

    return render(request, 'recipe_create.html', {'form': form})

def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if recipe.created_by != request.user:
        return HttpResponseForbidden("You are not allowed to edit this recipe.")

    if request.method == 'POST':
        form = Recipeform(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('userpage')
    else:
        form = Recipeform(instance=recipe)

    return render(request, 'edit_recipe.html', {'form': form})

def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    
    if recipe.created_by == request.user:
        recipe.delete()
        messages.success(request, "Recipe deleted successfully.")
    else:
        messages.error(request, "You are not authorized to delete this recipe.")
    
    return redirect('userpage')

def log_out(request):
    logout(request)
    return redirect('home')

