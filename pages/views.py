from django.shortcuts import render,redirect
from .models import Profile, Contact
from .forms import SignpForm, UserForm , ProfileForm, ContactForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form=SignpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('/profile')


    else:
        form=SignpForm

    return render(request,'signup.html',{'form':form})

def profile(request):
    profile=Profile.objects.get(user=request.user) 
    return render(request, 'profile.html', {'profile':profile})

def profile_edit(request):
    profile=Profile.objects.get(user=request.user)
    if request.method == 'POST':
        userform= UserForm(request.POST, instance=request.user)
        profileform=ProfileForm(request.POST, instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myform=profileform.save(commit=False)
            myform.user=request.user
            myform.save()
            return redirect('/profile')

    else:
        userform= UserForm(instance=request.user)
        profileform=ProfileForm(instance=profile)
    return render(request, 'profile_edit.html',{
        'userform': userform,
        'profileform':profileform

    })

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def portfilo(request):
    return render(request, 'portfilo.html')        
from django.http import JsonResponse

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {'success': True})
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})