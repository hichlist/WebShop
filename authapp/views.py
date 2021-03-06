from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.http import Http404
from authapp.forms import MyRegistrationForm

def login(request):
    if request.method == 'POST':
        print("POST data =", request.POST)
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("/")
        else:
            return render(request, 'mainapp/main.html', {'errors': True})
    raise Http404

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def registration(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        context = {'form': form}
        return render(request, 'authapp/registration.html', context)
    context = {'form': MyRegistrationForm()}
    return render(request, 'authapp/registration.html', context)
