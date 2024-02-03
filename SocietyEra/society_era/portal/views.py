from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import CreateUserForm, ReferenceId
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import random

@login_required(login_url='/login')
def community(request):
    return render(request, 'community.html')
def references(request):
    return render(request, 'references.html')
def services(request):
    return render(request, 'services.html')
def GenerateRefID(request):
    reference_id_number = None
    form = ReferenceId()
    
    if request.method == 'POST':
        form = ReferenceId(request.POST)
        reference_id_instance = form.save(commit=False)
        reference_id_instance.reference_id = random.randint(100000, 999999)
        reference_id_instance.save()
        reference_id_number = reference_id_instance.reference_id
    else:
        form = ReferenceId()         
    return render(request, 'generate_ref_id.html', {'form': form, 'reference_id_number': reference_id_number})

def First(request):
    return render(request, 'first.html')
def HomePage(request):
    return render(request, 'homepage.html')
def Register(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account is created for '+user)
            return redirect('login')
    
    context={'form':form}
    return render(request, 'register.html', context)
def Login(request):
    context={}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return render(request, 'login.html', context)
    
    return render(request, 'login.html', context)
