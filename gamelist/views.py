from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse_lazy, reverse

from django.views.generic import CreateView, DetailView, UpdateView
from django.views.generic.edit import FormView

from django.contrib.auth.models import User
from gamelist.models import GameList
from gamelist.forms import GameListCretionForm
from account.models import Member

from game.forms import GameCreationForm
from game.models import Game

# Create your views here.
class GameListCreateView(FormView):
    """displays form to create new game collections"""
    form_class = GameListCretionForm
    template_name = "gamelist/gamelist_form.html"
    pk   = None

 
    def get_context_data(self, **kwargs):
        context = super(GameListCreateView, self).get_context_data(**kwargs)

        context['form'] = GameListCretionForm()

        return context

    def form_valid(self, form):
        if self.request.method == "GET":
            return redirect("home")
        
        user = self.request.user
        if not user.is_authenticated:
            return redirect('account:login')

        name         = form.cleaned_data['name']
        description  = form.cleaned_data['description']

        if GameList.objects.filter(name=name.strip()).exists():          
            return render(self.request, 'gamelist/gamelist_form.html',
                        {'error':'Game collection already exists','form':form})
        
        # get member instance
        member = Member.objects.get(user__username=user.username)
        
        game_list = GameList.objects.create(
            name=name,
            description=description,
            owner=member
        )  

        self.pk = game_list.pk
        return super(GameListCreateView,self).form_valid(form)


    def get_success_url(self):
        return reverse("list:list_detail", kwargs={'pk':self.pk})
        

class GameListDetailView(DetailView):
    model = GameList

    def get_context_data(self, **kwargs):
        context = super(GameListDetailView, self).get_context_data(**kwargs)

        context['game_form'] = GameCreationForm()
        context['games']     = GameList.objects.get(pk=self.kwargs['pk']).game.all()

        # check if user is authenticated
        user = self.request.user
        if user.is_authenticated:
            if GameList.objects.filter(owner__user__username=user.username, pk=self.kwargs['pk']).exists():
                context['owner'] = True

        return context


class GameListUpdateView(UpdateView):
    model = GameList
    template_name = "gamelist/gamelist_update_form.html"
    form_class  = GameListCretionForm

    def get_context_data(self, **kwargs):
        context = super(GameListUpdateView, self).get_context_data(**kwargs)

        # check if user is authenticated
        user = self.request.user
        if user.is_authenticated:
            if GameList.objects.filter(owner__user__username=user.username, pk=self.kwargs['pk']).exists():
                context['owner'] = True
            else:
                return redirect('home')
        else:
            return redirect('account:login')
            
        return context
    

    

     

