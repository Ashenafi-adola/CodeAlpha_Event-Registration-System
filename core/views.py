from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Event
from .forms import EventForm
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class Registration(generic.CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'core/authPage.html'
    success_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'signup'
        return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class Home(generic.CreateView):
    model = Event
    form_class = EventForm
    template_name = 'core/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = self.get_queryset()
        return context

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)
    
    def form_valid(self, form):
        event = form.save(commit=False)
        event.user = self.request.user
        event.save()
        return redirect('/')