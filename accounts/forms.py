from django import forms
from django.forms import ModelForm
from .models import Ticket
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django import forms
class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        
class CreateTickeForm(ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        exclude = ['status','comment']
    
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'email', 'password1', 'password2']