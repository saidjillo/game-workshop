from django.conf.urls import url

from community.views import ForumDetailView, PostsCreateView, add_reply, ForumPageForm, ForumCreateView, AllForumsTemplateView

app_name = 'community'

urlpatterns = [
    url(r'^$', AllForumsTemplateView.as_view(), name="all_forums"),
    url(r'^forum/(?P<pk>\d+)/$', ForumDetailView.as_view(), name="forum"),
    url(r'^forum/game/(?P<pk>\d+)/(?P<slug>[-\w]+)/$', ForumPageForm.as_view(), name="forum_page"),
    url(r'^forum/(?P<pk>\d+)/(?P<slug>[-\w]+)/$', ForumCreateView.as_view(), name="forum_create"),
    url(r'^forum/(?P<pk>\d+)/post/create/$', PostsCreateView.as_view(), name="post_create"),
    url(r'^forum/post/reply/$', add_reply, name="post_reply"),
]