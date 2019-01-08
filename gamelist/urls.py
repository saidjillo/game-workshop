from django.conf.urls import url

from gamelist.views import GameListCreateView, GameListDetailView, GameListUpdateView

app_name = "list"

urlpatterns = [
    url(r'^list/create/$',GameListCreateView.as_view(),name='list_create'),
    url(r'^list/detail/(?P<pk>\d+)/$',GameListDetailView.as_view(),name='list_detail'),
    url(r'^list/update/(?P<pk>\d+)/$',GameListUpdateView.as_view(),name='list_update'),
]