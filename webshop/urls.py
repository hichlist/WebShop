"""webshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
import mainapp.views as mainapp
import authapp.views as authapp
import adminapp.views as adminapp

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin_page/$', adminapp.admin_page),
    url(r'^admin_page/delete/user/(\d+)$', adminapp.delete_user),
    url(r'^$', mainapp.main, name='main'),
    url(r'^item/(?P<id>\d+)$', mainapp.item, name='item'),
    url(r'^contact/$', mainapp.get_contact, name='contact'),
    url(r'^user/login/$', authapp.login, name='login'),
    url(r'^user/logout/$', authapp.logout, name='logout'),
    url(r'^user/registration/$', authapp.registration, name='registration'),
    # static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

