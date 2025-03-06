from django.shortcuts import render
from django.http import HttpResponse

def home(request):
 peoples=[
    {'name':'Abhijeet','age':'22'},
    {'name':'Hiren','age':'85'},
    {'name':'manvi','age':'11'},
    {'name':'Auras','age':'12'},
 ]

 vegetables=["Pumpkin","Tomato","Potato","Aloo Matar"]
 context={'page':'Django Tutorial'}
 return render (request,"index.html",context={'peoples':peoples,'vegetables':vegetables})

def success_page(request):
    print("*" *10)
    context={'page':'Success Page'}
    return HttpResponse("<h1>Hey This is a Success Page</h1>",context)

def contact(request):
   context={'page':'Contact'}
   return render(request,"contact.html",context)
def about(request):
   context={'page':'About'}
   return render(request,"about.html",context)