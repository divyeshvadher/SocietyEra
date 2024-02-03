import uuid
from socket import fromshare
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from portal.models import reference_id




        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class ReferenceId(forms.ModelForm):
    class Meta:
        model = reference_id
        fields = ["user", "contact", "address",]
        labels = {"user": "Name", "contact": "Contact", "address": "Address",} 
        
    
        
        
        