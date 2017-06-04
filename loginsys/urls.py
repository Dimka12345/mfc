from django.conf.urls import url

from django.conf.urls import url, include

#from loginsys import views
from django.contrib import admin
from django.contrib.auth import views

from django.conf.urls import url

from loginsys import models
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^register/', models.RegisterFormView.as_view(), name='register'),
]