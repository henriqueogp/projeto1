from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('The Homepage')


def contact(request):
    return HttpResponse('Contact info')
