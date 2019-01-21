from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
from itertools import chain

from django.views.generic import ListView

from gamelist.models import GameList
from game.models import Game, Ratings
from community.models import Forum
from blog.models import Blog

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
        forums    = Forum.objects.filter(topic__icontains=self.request.GET.get('q'))
        blogs     = Blog.objects.filter(title__icontains=self.request.GET.get('q'))

        query = chain(games,gameslist,forums,blogs)
        context['results'] = sorted(query, 
            key=lambda instance: instance.pk, 
            reverse=True)

        return context


def confirmation(request):
    response = {
        "ResultCode":0,
        "ResultDesc":"Confirmation received successfully"
    }

    # obtaining data from mpesa

    return render(request, 'confirmation.html', {'response': response})


def validation(request):
    response = {
        "ResultCode":0,
        "ResultDesc":"Confirmation received successfully"
    }

    # obtaining data from mpesa

    return render(request, 'confirmation.html', {'response': response})


def register_url(request):
    # mpesa making requests to get access token
    import requests
    from requests.auth import HTTPBasicAuth
    import json


    consumer_key = 'ojDr5pKayBHvpGh3aQt27GMr5ZialWYq'
    consumer_secret_key = 'QqFQJAyJZLpod5QK'

    # url
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret_key))


    json_data = json.loads(r.text)
    access_token = json_data.get('access_token', None)

    api_url = "http://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = { "ShortCode": "174379",
        "ResponseType": "Confirmed",
        "ConfirmationURL": "http://127.0.0.1:8000/confirmation",
        "ValidationURL": "http://127.0.0.1:8000/validation_url"}

    response = requests.post(api_url, json = request, headers=headers)

    print (response.text)

    
    
 

