from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
def home(request):
    return render(request,'web page\home.html')
def contact(request):
    return render(request,'web page\contact.html')
def about(request):
    return render(request,'web page\About.html')