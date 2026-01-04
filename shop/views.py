from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'shop/home.html')

def detail_product(request):
    return render(request, 'shop/detail_product.html')
