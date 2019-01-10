# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.translation import ugettext as _

from .models import VisitorMessage, Location
def index(request):
    from django.utils import translation

    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]
    #language = translation.get_language_from_request(request)
    return render(request, 'index.html')

def add(request):
    if(request.method == 'POST'):
        newtitle = request.POST['title']
        newtext = request.POST['text']
        visitorMessage = VisitorMessage(title=newtitle, text=newtext)
        visitorMessage.save()

def home(request):
    cabin_location = Location.objects.get(name='hommalinna')
    context = {
        'cabin_location' : cabin_location
    }
    return render(request, 'home.html', context)

def landscape(request):
    cabin_location = Location.objects.get(name='hommalinna')
    context = {
        'cabin_location' : cabin_location
    }
    return render(request, 'landscape.html', context)

def cabin(request):
    cabin_location = Location.objects.get(name='hommalinna')
    context = {
        'cabin_location' : cabin_location
    }
    return render(request, 'home.html', context)

def guestbook(request):
    cabin_location = Location.objects.get(name='hommalinna')
    context = {
        'cabin_location' : cabin_location
    }
    return render(request, 'home.html', context)

def location(request):
    cabin_location = Location.objects.get(name='hommalinna')
    context = {
        'cabin_location' : cabin_location
    }
    return render(request, 'location.html', context)

def gmaps(request):
    cabin_location = Location.objects.get(name='hommalinna')
    context = {
        'cabin_location' : cabin_location
    }
    return render(request, 'gmaps.html', context)
