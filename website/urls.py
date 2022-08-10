from django.contrib import admin
from django.urls import path
from website.views import http_test,json_test

urlpatterns = [
    path('',http_test),
    path('json-test',json_test)
]
