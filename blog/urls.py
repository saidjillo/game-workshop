from django.conf.urls import url

from blog.views import BlogListView,BlogDetailView

app_name = 'blog'

urlpatterns = [
    url(r'^$', BlogListView.as_view(), name="blogs"),
    url(r'^(?P<pk>\d+)/(?P<slug>[-\w]+)/$', BlogDetailView.as_view(), name="blog_detail"),
]