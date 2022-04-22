from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _

def testlang(request):
    return HttpResponse(_('Welcome to language translation'))

def index(request):
    return render(request, 'index.html')

def Events(request):
    return render(request, 'Events.html')


def News(request):
    return render(request, 'News.html')


def Sports(request):
    return render(request, 'Sports.html')


def ContactUs(request):
    return render(request, 'ContactUs.html')

def Form(request):
    return render(request, 'Form.html')


