from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import render
from mainapp.models import Product
from django.contrib import auth
from django.http import Http404
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

def admin_page(request):
    # TODO: сделать доступ у админке только суперпользователю
    users = User.objects.all()
    return render(request, 'adminapp/admin_page.html', {'users': users})

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return HttpResponseRedirect('/admin')
