from django.contrib import admin
from django.urls import path
from website.views import home,contact,about

urlpatterns = [
    path('',home),
    path('contact',contact),
    path('about',about)
]
