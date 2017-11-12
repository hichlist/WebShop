from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import render
from mainapp.models import Product
from django.contrib import auth
from django.http import Http404

# Create your views here.
def main(request):
    product = Product.objects.all()
    product_top = Product.objects.all()[:3]
    product_sale = Product.objects.all()[3:6]
    
    return render(request, 'mainapp/main.html', {'product': product, 'product_top': product_top, 'product_sale': product_sale})

def login(request):
    if request.method == 'POST'
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        
    