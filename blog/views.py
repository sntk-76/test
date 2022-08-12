from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
def blog_home(request):
    return render(request,'blog\Blog-home.html')
def blog_single(request):
    return render(request,'blog\Blog-single.html')

# Create your views here.
