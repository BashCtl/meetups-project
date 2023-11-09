from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Meetup

# Create your views here.


def index(request):
    meetups = Meetup.objects.all()
    context = {'meetups': meetups}
    return render(request, 'meetups/index.html', context)


def meetup_details(request, slug):
    try:
        meetup = Meetup.objects.get(slug=slug)
    
        context = {'meetup': meetup, 'meetup_found': True}
        return render(request, 'meetups/meetup-detail.html', context)
    except Exception as e:
        return render(request, 'meetups/meetup-detail.html', {'meetup_found': False})
