from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Meetup
from .forms import RegistrationForm

# Create your views here.


def index(request):
    meetups = Meetup.objects.all()
    context = {'meetups': meetups}
    return render(request, 'meetups/index.html', context)


def meetup_details(request, slug):
    try:
        meetup = Meetup.objects.get(slug=slug)
        if request.method == 'GET':
            form = RegistrationForm()
        else:
            form = RecursionError(request.POST)
            if form.is_valid():
                participant = form.save()
                meetup.participants.add(participant)
                return redirect

        context = {'meetup': meetup, 'meetup_found': True, 'form': form}
        return render(request, 'meetups/meetup-detail.html', context)
    except Exception as e:
        return render(request, 'meetups/meetup-detail.html', {'meetup_found': False})
