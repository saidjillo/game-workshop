from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.forms.formsets import formset_factory
from django.db import IntegrityError, transaction

from django.views.generic import CreateView,UpdateView,ListView, UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from account.forms import UserSignUpForm, LoginForm, ProfileForm, PictureForm
from gamelist.models import GameList
from game.models import Game
from account.models import Member


# Create your views here.
class SignUp(CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy('account:login')
    template_name = 'account/signup.html'


def login_view(request):
    form = LoginForm()

    if request.user.is_authenticated:
        return redirect("home")
    return render(request, 'account/login.html', {'form':form})


def login_user(request):
    form = LoginForm(request.POST or None)
    print(form.data)
    if request.method == "POST" and form.is_valid() :       
        username = form.data['username']
        password = form.data['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            form = LoginForm()
            return render(request, "account/login.html", {"form":form,"error":"Invalid username or password"})
    return render(request, "account/login.html")

    if request.method == "GET":
        return redirect("home")



def logout_view(request):
    logout(request)
    return redirect("account:login")


def dashboard_view(request, username):
    if request.method == "POST":
        return HttpResponse(status=500)

    if request.method == "GET":
        user = request.user
    
    if not user.is_authenticated:
        return redirect('account:login')
    
    game_lists = GameList.objects.filter(owner__user__username=user.username)
    games = GameList.objects.filter(owner__user__username=user.username)
    return render(request, 'account/dashboard.html', {'game_lists':game_lists,'games':games})


def profile_page(request, username):
    """
    Allows a user to update their own profile.
    """
    # capture and set user in session
    user = request.user

    if request.method == "GET":
         
        if not user.is_authenticated:
            # very username if exists
            try_user = User.objects.filter(username=username)
            if not try_user.exists():
                return render(request,'404.html')
            
            user_obj = User.objects.get(username=username)
            return render(request, 'account/profile.html', {'user_obj':user_obj})

        else:
            # check if user is equal to username
            if user.username == username:  
                # Create the formset, specifying the form and formset we want to use.        
                PictureFormSet = formset_factory(PictureForm)
                profile_form = ProfileForm(request.POST, user=user)
                picture_formset = PictureFormSet(request.POST, request.FILES)

                user_obj = User.objects.get(username=username)
                profile_form = ProfileForm(user=user)
                picture_formset = PictureFormSet()

                return render(request, 'account/profile.html', 
                    {'user_obj':user_obj,
                    'status':True,
                    'profile_form':profile_form, 
                    'picture_formset':picture_formset})

            user_obj = User.objects.get(username=username)
            return render(request, 'account/profile.html', {'user_obj':user_obj})
                

    if request.method == 'POST':
        if not user.is_authenticated:
            return redirect('account:login')
        
        else:         
            if user.username == username:

                # Create the formset, specifying the form and formset we want to use.        
                PictureFormSet = formset_factory(PictureForm)
                profile_form = ProfileForm(request.POST, user=user)
                picture_formset = PictureFormSet(request.POST, request.FILES)

                if profile_form.is_valid() and picture_formset.is_valid():
                    # save user info
                    user.first_name = profile_form.cleaned_data.get('first_name')
                    user.last_name  = profile_form.cleaned_data.get('last_name')
                    user.save()

                    # now save data for picture_form
                    for picture_f in picture_formset.cleaned_data:           
                        picture = picture_f.get('pic', None)
                        proffession = picture_f.get('proffession', None)

                        if proffession is not None:  
                            if len(proffession) > 0:                       
                                member_obj = Member.objects.get(user__username=username)
                                member_obj.proffession = proffession
                                member_obj.save()
            
                        if picture:                   
                            member_obj = Member.objects.get(user__username=username)
                            member_obj.pic = picture
                            member_obj.save()

                    return redirect('account:profile', username=user.username)

            
            else:
                return render(request, '404.html')


        

      
   
        
        


