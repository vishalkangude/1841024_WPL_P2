from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homePageView(request):
    return HttpResponse('Hello!!!, This is VISHAL KANGUDE from T2 Batch and my PRN is 1841024')
