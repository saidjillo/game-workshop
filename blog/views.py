from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView

from blog.models import Blog, BlogMedia
from community.models import Forum
from game.models import Game
from gamelist.models import GameList

# Create your views here.
class BlogListView(ListView):
    model = Blog
    template_name =       "blog/blog.html"
    context_object_name = 'blogs'
 
    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)

        context['myblog'] = Blog.objects.all().order_by('id')[:1]
        context['forums'] = Forum.objects.all().order_by('-id')[:10]
        context['games']  = Game.objects.all().order_by('-id')[:5]
        context['collections']  = GameList.objects.all().order_by('-id')[:5]
        return context

class BlogDetailView(DetailView):
    model         = Blog
    template_name = 'blog/blog_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)

        context['forums'] = Forum.objects.all().order_by('-id')[:10]

        # get first letter of the current object
        first_letter = self.get_object().title[0]
        context['blogs'] = Blog.objects.filter(title__icontains=first_letter).exclude(pk=self.get_object().pk)

        return context


        


