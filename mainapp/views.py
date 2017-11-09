from django.shortcuts import render
from mainapp.models import Product

# Create your views here.
def main(request):
    product = Product.objects.all()
    product_top = Product.objects.all()[:3]
    product_sale = Product.objects.all()[3:6]
    
    return render(request, 'mainapp/main.html', {'product': product, 'product_top': product_top, 'product_sale': product_sale})