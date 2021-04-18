from django.shortcuts import render
from django.http import HttpResponse
from pharmasite.models import Products


def home(request):
    products = Products.objects.all()
    context = {
        'products':products
    }
    return render(request, "index.html",context)

def products(request):
    products = Products.objects.all()
    context = {
        'products':products
    }
    
    return render(request, "shop.html", context)

def selected_product(request,medicine_name):
    selected_product = Products.objects.get(slug=medicine_name)

    return render(request, "shop-single.html",{'selected_product':selected_product})



