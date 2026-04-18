from . models import Event
from django.forms import ModelForm, Textarea, TextInput, CheckboxInput


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'completed']
        widgets = {
            'title': TextInput(attrs=({
                'class':'form-control',
                'placeholder': "Enter Title"
            })),
            'description': Textarea(attrs=({
                'class': 'form-control',
                'placeholder': "Enter The Description...",
                'rows': 4
            }))
        }
