from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from . models import Event
from .forms import EventForm
from django.views import generic



class Home(generic.CreateView):
    model = Event
    form_class = EventForm
    template_name = 'core/index.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)