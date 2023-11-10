from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Meetup, Participant
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
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user_email = form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                meetup.participants.add(participant)
                return redirect('confirm-registration')
        context = {'meetup': meetup, 'meetup_found': True, 'form': form}
        return render(request, 'meetups/meetup-detail.html', context)
    except Exception as e:
        print(e)
        return render(request, 'meetups/meetup-detail.html', {'meetup_found': False})


def confirm_registration(request):
    return render(request, 'meetups/registration-success.html')
