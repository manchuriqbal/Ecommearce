from django.shortcuts import render
from .models import Product

def view_product(request, slug):
    try:
        product = Product.objects.get(slug = slug)
        return render(request, "product/product.html", context= {"product" : product})
    except Exception as e:
        print(e)