from django.conf.urls import url

from game.views import GameCreateView, GameDetailView, game_add_form_view,GameDeleteView

app_name = 'game'

urlpatterns = [
    url(r'^(?P<list_pk>\d+)/$', GameCreateView.as_view(), name="game_create"),
    url(r'^detail/(?P<pk>\d+)/$', GameDetailView.as_view(), name="game_detail"),
    url(r'^delete/(?P<pk>\d+)/$', GameDeleteView.as_view(), name="game_delete"),
    url(r'^(?P<game_list_pk>\d+)/game/add/$', game_add_form_view, name="game_add"),
]