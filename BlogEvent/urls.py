from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin'),
    path('', views.home, name='base'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
]