from django.shortcuts import render ,redirect
from django.urls import reverse
from .forms import SignupForm,ProfileForm,UserForm
from .models import Profile
from django.contrib.auth import authenticate , login
# Create your views here.

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect(reverse("accounts:profile"))
    else:
        form=SignupForm()
        
    return render(request,"registration/signup.html",{'form':form})

def profile(request):
    profile=Profile.objects.get(user=request.user)
    
    return render(request,"profile/profile.html",{"profile":profile})

def profile_edit(request):
     profile=Profile.objects.get(user=request.user)
     if request.method=="POST":
         user_form=UserForm(request.POST,instance=request.user)
         profile_form=ProfileForm(request.POST,request.FILES,instance=profile)
         if user_form.is_valid() and  profile_form.is_valid():
             user_form.save()
             profile_form.save(commit=False)
             profile_form.user=request.user
             profile_form.save()
             
             return redirect(reverse("accounts:profile")) 
             
     else:
         user_form=UserForm(instance=request.user)
         profile_form=ProfileForm(instance=profile)
    
     return render(request,"profile/profile_edit.html",{'user_form':user_form,'profile_form':profile_form})
         