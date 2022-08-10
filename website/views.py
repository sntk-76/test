from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
def http_test(request):
    return HttpResponse('<h1> Hi dear</h1>')
def json_test(request):
    return JsonResponse({'sina' : '25'})    