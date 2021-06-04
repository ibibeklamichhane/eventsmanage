from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def about(request):
    return render(request, 'eventmanage/about.html')

def get_all_events(request):
    event = Event.objects.all()
    return render(request, 'eventmanage/event.html',{"data":event})

    