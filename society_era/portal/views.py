from email import message
import secrets
from django.shortcuts import render, redirect
from .forms import CreateUserForm, ReferenceId, CommunityForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import reference_id, Community
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

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
            messages.success(request, f'Community "{community}" created successfully!')
            return redirect('community')
        else:
            messages.error(request, 'Please correct the form errors.')

    else:
        form = CommunityForm()

    return render(request, 'community.html', {'community_form': form})

@login_required(login_url='/login')
def join_community(request, reference_id):
    if request.method == 'POST':
        try:
            reference_id_value = request.POST.get('reference_id')
            community = get_object_or_404(Community, id=reference_id)
            user_reference_instance = get_object_or_404(reference_id, user=request.user, reference_id=reference_id_value, community=None)

            if user_reference_instance.user == request.user.username:
                user_reference_instance.community = community
                user_reference_instance.save()
                messages.success(request, f'You have joined the {community.name} community!')
                community.is_user_member = True
                community.save()
                return JsonResponse({'is_user_member': community.is_user_member})
            else:
                messages.error(request, 'Invalid Reference ID. Please Try Again.')
                return JsonResponse({'error': 'Invalid Reference ID'})
        except:
            message.error(request, 'Invalid Request. Please Try Again.')
            return JsonResponse({'error': 'Invalid Request'})
    return redirect('community')  
@login_required(login_url='/login')
def references(request):
    user_reference_id = None
    
    
    if request.user.is_authenticated:
        try:
            user_reference_instance = reference_id.objects.get(user=request.user)
            user_reference_id = user_reference_instance.reference_id
        except reference_id.DoesNotExist:
            pass

    return render(request, 'references.html', {'user_reference_id': user_reference_id})

@login_required(login_url='/login')
def services(request):
    return render(request, 'services.html')


def GenerateRefID(request):
    reference_id_number = None

    if request.method == 'POST':
        form = ReferenceId(request.POST)
        if form.is_valid():
            reference_id_instance = form.save(commit=False)
            community_id = request.POST.get('community_id')
            if community_id:
                community = Community.objects.get(id=community_id)
                reference_id_instance.community = community
            reference_id_instance.user = request.user    
            reference_id_instance.reference_id = secrets.token_urlsafe(6)
            reference_id_instance.save()            
            reference_id_number = reference_id_instance.reference_id
            messages.success(request, 'Reference ID generated successfully!')
            return redirect('community')
            
        
    else:
        form = ReferenceId()
    return render(request, 'generate_ref_id.html', {'form': form, 'reference_id_number': reference_id_number})

def HomePage(request):
    return render(request, 'homepage.html')

def Register(request):
    form = CreateUserForm()
    context={}
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account is created for ' + user.username)
            return redirect('login')
        
    
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
            return redirect('home')
            # return JsonResponse({'success': True, 'username': user.username})
        else:
            messages.info(request, 'Username or Password is incorrect')
            return JsonResponse({'success': False, 'message': 'Username or Password is incorrect'})
    
    return render(request, 'login.html', context)

def Logout(request):
    logout(request)
    return redirect('home')
