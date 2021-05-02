from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('pubg',views.pubg,name='pubg'),
    path('valorant',views.valorant,name='valorant'),
    path('contact',views.contact,name='contact'),

]
