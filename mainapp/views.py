from django.shortcuts import render
from mainapp.models import Product
from django.contrib import auth
from django.http import Http404, HttpResponseRedirect

from .forms import ContactForm
from .models import Contact


# Create your views here.
def main(request):
    product = Product.objects.all()
    product_top = Product.objects.all()[:3]
    product_sale = Product.objects.all()[3:6]
    return render(request, 'mainapp/main.html', {'product': product, 'product_top': product_top, 'product_sale': product_sale})


def item(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'mainapp/item.html', {'product': product})


def get_contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # sender = form.cleaned_data['sender']
            # subject = form.cleaned_data['subject']
            # message = form.cleaned_data['message']
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()

    return render(request, 'mainapp/contact.html', {'form': form})
