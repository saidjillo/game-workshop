"""workshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

from workshop.main_view import GameListView, AllGamesListView,SearchListView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', GameListView.as_view(), name="home"),
    url(r'^games/game/all/$', AllGamesListView.as_view(), name="all_games"),
    url(r'^search/$', SearchListView.as_view(), name="search"),
    url(r'account/', include('account.urls', namespace="account")),
    url(r'^games/', include('gamelist.urls', namespace="my_list")),
    url(r'^game/', include('game.urls', namespace="game")),
]

if not settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
