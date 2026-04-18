from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Event
from .forms import EventForm
from django.views import generic

class Registration(generic.CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'core/authPage.html'
    success_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'signup'
        return context

class Home(generic.CreateView):
    model = Event
    form_class = EventForm
    template_name = 'core/index.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)