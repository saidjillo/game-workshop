from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy, reverse

from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import FormView

from game.forms import GameCreationForm

from gamelist.models import GameList
from django.contrib.auth.models import User
from account.models import Member
from game.models import Game, HitCount

# Create your views here.
class GameCreateView(FormView):
    form_class    = GameCreationForm
    pk            = None

    def form_valid(self, form):
        if self.request.method == "GET":
            return redirect('home')

        user = self.request.user
        if not user.is_authenticated:
            return redirect('account:login')

        # check if list with list_pk and user exist
        owner = Member.objects.get(user__username=user.username)
        if GameList.objects.filter(pk=self.kwargs['list_pk'],owner=owner).exists():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            game_developer = form.cleaned_data['game_developer']
            url = form.cleaned_data['url']
            image_cover = form.cleaned_data['image_cover']

            # create game
            game = Game.objects.create(
                title = title,
                description =description,
                game_developer =game_developer,
                url =url,
                image_cover =image_cover,
                game_list=GameList.objects.get(pk=self.kwargs['list_pk'])
            )
            
            self.pk = game.pk
            return super(GameCreateView, self).form_valid(form)
        else:
            HttpResponse(status=500)

    def get_success_url(self):

        return reverse("game:game_detail", kwargs={'pk':self.pk})
            
            

class GameDetailView(UpdateView,DetailView):
    model = Game
    # fields = ['title','description','game_developer','url','image_cover'] cannot specify both fields and form_class together
    template_name = "game/game_detail.html"
    form_class = GameCreationForm
 

    def get_context_data(self, **kwargs):
        context = super(GameDetailView, self).get_context_data(**kwargs)

        context['game_list'] = Game.objects.get(pk=self.kwargs['pk']).game_list
        # context['form']      = GameCreationForm()
        name = self.get_object().title
        first_letter = name[0]
        
        # check if user is authenticated
        user = self.request.user
        if user.is_authenticated:
            if GameList.objects.filter(owner__user__username=user.username, pk=context['game_list'].pk).exists():
                context['owner'] = True
 
        context['related_games'] = Game.objects.filter(title__icontains=first_letter)[:8]

        game = self.get_object()
        hit = HitCount.objects.create(
            game=game
        )
        hit.increase_hit()

        return context

   
        
    def get_success_url(self):
        return reverse_lazy('game:game_detail', kwargs={'pk':self.get_object().pk})

  
        
class GameDeleteView(DeleteView):
    model = Game
    
    def get_success_url(self):
        game_list_pk = self.get_object().game_list.pk
        return reverse_lazy('list:list_detail', kwargs= {'pk':game_list_pk})



def game_add_form_view(request, game_list_pk):
    if request.method == 'POST':
        return HttpResponse(status=500)

    if request.method == 'GET':
        user = request.user
    
    if not user.is_authenticated:
        return redirect('account:login')

    # check if user has a game collection
    if GameList.objects.filter(owner__user__username=user.username, pk=game_list_pk).exists():
        gamelist = GameList.objects.get(pk=game_list_pk)
        game_form = GameCreationForm()
        return render(request, 'game/game_form.html' , {'gamelist':gamelist,'game_form':game_form})
    else:
        return redirect('list:list_create')


# def rate_game(request, pk):
#     if request.method == 'GET':
#         return HttpResponse(status=500)
    
#     if request.method == 'POST':
#         user = request.user
    
#     if not user.is_authenticated:
#         return JsonResponse({'error':'UnAuthorized request'})

#     if Game.objects.get(pk=pk).exists():
#         rate = Ratings.objects.create(
#             user = Member.objects.get(pk=pk),
#             game = Game.objects.get(pk=pk),
#             stars= 
#         )
           
#     else:
#         return HttpResponse(status=500)