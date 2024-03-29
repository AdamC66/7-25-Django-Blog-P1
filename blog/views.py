from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def root(request):
    return HttpResponseRedirect('home')

def home(request):
    context = {'date' : datetime.today().strftime('%Y-%m-%d')}
    response = render(request, 'index.html', context)
    return HttpResponse(response)