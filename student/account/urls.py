from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.mainhome,name='mainhome'),
    path('contact',views.contact,name='contact'),
    path('course',views.course,name='course'),
    path('gallery',views.Gallery,name='gallery'),
    path('index',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('forget',views.forget,name='forget'),
    
]
