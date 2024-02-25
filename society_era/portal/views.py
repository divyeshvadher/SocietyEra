import os
from django.conf import settings
import uuid
import qrcode
from django.shortcuts import render, redirect
from .forms import CreateUserForm, ReferenceId, CommunityForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import reference_id, Community
from django.contrib.auth.models import User
import random

@login_required(login_url='/login')
def community(request):
    
    user_communities = Community.objects.filter(president=request.user)
    
    all_communities = Community.objects.exclude(president=request.user)
    return render(request, 'community.html', {'user_communities': user_communities, 'all_communities': all_communities})

@login_required(login_url='/login')
def build_community(request):
    if request.method == 'POST':
        form = CommunityForm(request.POST)
        if form.is_valid():         
            community = Community.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                president=request.user
            )
            
            community.generate_qr_code()
            
            messages.success(request, f'Community "{community}" created successfully!')
            return redirect('community')
        else:
            messages.error(request, 'Please correct the form errors.')

    else:
        form = CommunityForm()

    return render(request, 'community.html', {'community_form': form})
def references(request):
    user_reference_id = None
    
    # Assuming you have a reference model and the user is authenticated
    if request.user.is_authenticated:
        try:
            user_reference_instance = reference_id.objects.get(user=request.user)
            user_reference_id = user_reference_instance.reference_id
        except reference_id.DoesNotExist:
            pass

    return render(request, 'references.html', {'user_reference_id': user_reference_id})

def services(request):
    return render(request, 'services.html')

def GenerateRefID(request):
    reference_id_number = None

    if request.method == 'POST':
        form = ReferenceId(request.POST)
        if form.is_valid():
            reference_id_instance = form.save()            
            reference_id_number = reference_id_instance.reference_id
            
        else:
            pass
        
    else:
        form = ReferenceId()
    return render(request, 'generate_ref_id.html', {'form': form, 'reference_id_number': reference_id_number})

def HomePage(request):
    return render(request, 'homepage.html')

def Register(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account is created for ' + user.username)
            return render(request, 'login.html', context)
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    
    context = {'form': form}
    return render(request, 'register.html', context)

def Login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return render(request, 'homepage.html', context)
            # return JsonResponse({'success': True, 'username': user.username})
        else:
            messages.info(request, 'Username or Password is incorrect')
            return JsonResponse({'success': False, 'message': 'Username or Password is incorrect'})
    
    return render(request, 'login.html', context)

def Logout(request):
    logout(request)
    return redirect('home')
