from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
def recipies(request):
    if request.method=="POST":
        data=request.POST
        recipe_name=data.get('recipe_name')
        recipe_description=data.get('recipe_description')    
        recipe_image=request.FILES.get('recipe_image')
        Recipe.objects.create(
        recipe_name=recipe_name,
        recipe_description=recipe_description,
        recipe_image=recipe_image
        )
        return redirect('/recipies')
    queryset=Recipe.objects.all()
    if request.GET.get('search'):
        
        queryset=queryset.filter(recipe_name__icontains=request.GET.get('search'))
    context={'recipies':queryset}
    return render(request,'recipies.html',context)

def delete_recipe(request,id):
     queryset=Recipe.objects.get(id=id)

     queryset.delete()     
     return redirect('/recipies')

def update_recipe(request,id):
    queryset=Recipe.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        recipe_image=request.FILES.get('recipe_image')
        recipe_description=data.get('recipe_description')
        recipe_name=data.get('recipe_name')

        queryset.recipe_name=recipe_name
        queryset.recipe_description=recipe_description

        if recipe_image:
            queryset.recipe_image=recipe_image

        queryset.save() 
        return redirect('/recipies/')
    context={'recipe':queryset}
    return render(request,'update-recipe.html',context)

