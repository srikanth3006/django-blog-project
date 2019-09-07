"""mysite URL Configuration

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
from django.conf.urls import url, include
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import login, logout
from blog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('', include('blog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # url('', include('django.contrib.auth.urls')),
    # url(r'accounts/login', login, name='login'),
    # url(r'accounts/logout', logout, name='logout', kwargs={'next_page': '/'}),
]
