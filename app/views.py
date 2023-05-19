from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def wish(request,na):
    return HttpResponse(f'Hai Mr/Ms {na}')