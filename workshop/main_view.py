from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
from itertools import chain

from django.views.generic import ListView

from gamelist.models import GameList
from game.models import Game, Ratings

# main view starts here
class GameListView(ListView):
    model = GameList
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(GameListView, self).get_context_data(**kwargs)

        context['games'] = Game.objects.all()
        context['collections'] = GameList.objects.all()

        all_lists = GameList.objects.all()
        paginator = Paginator(all_lists, 7)
        page      = self.request.GET.get('page')

        all_game_list = paginator.get_page(page)
        context['all_game_list'] = all_game_list
  
        return context

class AllGamesListView(ListView):
    model               = Game
    template_name       = 'games.html'
    context_object_name = 'games'

    def get_context_data(self, **kwargs):
        context = super(AllGamesListView, self).get_context_data(**kwargs)

        context['gameslist'] = GameList.objects.all()[:5]
        return context
    

class SearchListView(ListView):
    model = GameList
    template_name = "search.html"

    def get_context_data(self, **kwargs):
        context = super(SearchListView, self).get_context_data(**kwargs)

        
        games     = Game.objects.filter(title__icontains=self.request.GET.get('q'))
        gameslist = GameList.objects.filter(name__icontains=self.request.GET.get('q'))

        query = chain(games,gameslist)
        context['results'] = sorted(query, 
            key=lambda instance: instance.pk, 
            reverse=True)

        return context




    
    
    
 

