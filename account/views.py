from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

from django.views.generic import CreateView,UpdateView,ListView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from account.forms import UserSignUpForm, LoginForm
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
