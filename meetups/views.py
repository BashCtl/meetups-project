from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    meetups = [
        {'pk': 1, 'title': 'A First Meetup',
            'location': 'New York', 'slug': 'a-first-meetup'},
        {'pk': 1, 'title': 'A Second Meetup',
            'location': 'Paris', 'slug': 'a-second-meetup'}
    ]
    context = {'meetups': meetups}
    return render(request, 'meetups/index.html', context)


def meetup_details(request, slug):
    meetup = {'title': 'A First Meetup',
              'description': 'This is the first meetup!'}
    context = {'meetup': meetup}
    return render(request, 'meetups/meetup-detail.html', context)
