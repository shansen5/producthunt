from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def home( request ):
    products = Product.objects
    return render( request, 'products/home.html', {'products':products} )

def blogs( request ):
    return render( request, 'products/blogs.html' )