from dataclasses import field
from pickle import FALSE
import uuid
from socket import fromshare
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Community, reference_id

from portal.models import reference_id

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class ReferenceId(forms.ModelForm):
    user = forms.CharField(max_length=100, required=True, label='Full Name')
    class Meta:
        model = reference_id
        fields = ["user", "contact", "address",]
        labels = {"user": "Name", "contact": "Contact", "address": "Address",} 
        
    # def save(self, commit=True):
    #     user = User.objects.create(username=self.cleaned_data['full_name'])
    #     reference_id_instance = super(ReferenceId, self).save(commit=False)
    #     reference_id_instance.user = user
    #     if commit:
    #         reference_id_instance.save()
    #     return reference_id_instance
    
class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ['name', 'description']
        
        
        
