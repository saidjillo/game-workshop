from django.shortcuts import render, redirect, render_to_response
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.views.generic import DetailView, CreateView, TemplateView
from django.views.generic.edit import FormView

from community.models import Forum, ReplyToPost, Posts
from django.contrib.auth.models import User
from game.models import Game
from gamelist.models import GameList
from account.models import Member

from community.forms import PostCreationForm, ForumCreationForm

# Create your views here.

 
class ForumDetailView(DetailView):
    model = Forum
    template_name = "community/forum.html"

    def get_context_data(self, **kwargs):
        context = super(ForumDetailView,self).get_context_data(**kwargs)
        context['form'] = PostCreationForm()

        # get first letter of the current object
        first_letter = self.get_object().topic[0]
        context['related_topics'] = Forum.objects.filter(topic__icontains=first_letter).exclude(pk=self.get_object().pk)[:10]

        return context

class AllForumsTemplateView(TemplateView):
    template_name = 'community/all_forums.html'

    def get_context_data(self, **kwargs):
        context = super(AllForumsTemplateView, self).get_context_data(**kwargs)

        context['forums'] = Forum.objects.all()
        return context
    


class ForumPageForm(TemplateView):
    template_name = "community/create_forum.html"

    def get_context_data(self, **kwargs):
        context = super(ForumPageForm, self).get_context_data(**kwargs)

        context['form'] = ForumCreationForm()
        context['game'] = Game.objects.get(pk=self.kwargs['pk'])
        
        return context



class ForumCreateView(FormView):
    form_class = ForumCreationForm
    pk         = None

    def form_valid(self, form):
        if self.request.method == 'GET':
            return render(request, '404.html')

        user = self.request.user
        if not user.is_authenticated:
            return redirect('account:login')

        if not Game.objects.filter(pk=self.kwargs['pk']).exists():
            return render(request, '404.html')

        game = Game.objects.get(pk=self.kwargs['pk'])
        topic= form.cleaned_data['topic']
        members = Member.objects.filter(user__username=user.username)

        if len(topic.strip()) == 0 or topic is None:
            return redirect('community:forum_page', pk=game.pk, slug=game.slug)

        forum = Forum.objects.create(
                    game= game,
                    forum_admin=User.objects.get(pk=user.pk),
                    topic=topic
                )
        for m in members:
            forum.member.add(m)

        self.pk = forum.pk
        return super(ForumCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('community:forum', kwargs={'pk': self.pk})       

    
class PostsCreateView(FormView):
    form_class = PostCreationForm

    def form_valid(self, form):
        if self.request.method == 'GET':
            return redirect('home')
        
        user = self.request.user
        if not user.is_authenticated:
            return redirect('account:login')

        post = form.cleaned_data['post']
        if len(post.strip()) == '' or post == None:
            messages.add_message(self.request, messages.INFO, 'Make sure your post is not empty')
            return redirect('community:forum', pk=self.kwargs['pk'])

        # create post
        forum       = Forum.objects.get(pk=self.kwargs['pk'])
        post_owner  = Member.objects.get(user__pk=user.pk)

        Posts.objects.create(
            forum=forum,
            post_owner=post_owner,
            post=post
        )

        return super(PostsCreateView, self).form_valid(form)
    def get_success_url(self):
        return reverse("community:forum", kwargs={'pk':self.kwargs['pk']})



@csrf_exempt
def add_reply(request):
    if request.method == 'GET':
        return render(request, '404.html')

    user = request.user
    if request.is_ajax():       
        forum_id = request.POST.get('forum_pk')
        post_pk =  request.POST.get('post_pk')

    if not user.is_authenticated:
        return redirect('account:login')

    try:
        forum = Forum.objects.get(pk=forum_id)
        post  = Posts.objects.get(pk=post_pk)

    except Exception as e:
        response = JsonResponse({'status':False,'error':'Not Found at all'})
        response.status_code = 404
        return response

    reply = request.POST.get('reply', None)
    if len(reply.strip()) == '' or reply == None:
        response = JsonResponse({'status':False,'error':'post cannot be empty'})
        response.status_code = 304
        return response

    try:
        reply_obj = ReplyToPost.objects.create(
            post=post,
            owner= Member.objects.get(user__pk=user.pk),
            reply= reply
        )
        reply_obj.save()

        response = render_to_response('community/ajax/replier.html',{'status':True,'success':'post created.','reply':reply_obj})
        response.status_code = 201
        return response

    except Exception as e:
        response = JsonResponse({'status':False,'error':'We could not submit your comment please try later.'})
        response.status_code = 304
        return response


def delete_post(request, post_pk, forum_pk):
    if request.method == 'GET':
        return render(request, '404.html')

    user = request.user
    if not user.is_authenticated:
        return redirect('account:login')

    # check if post belongs to user
    owner = False
    if Posts.objects.filter(post_owner__user__pk=user.pk, pk=post_pk).exists():
        post = Posts.objects.get(pk=post_pk)
        owner = True
    else:
        owner = False

    if Forum.objects.filter(pk=forum_pk, member__user__pk=user.pk).exists():
        if  post in Forum.objects.get(pk=forum_pk).posts.all:
            owner = True
        else:
            owner = False
    else:
        owner = False

    if owner == True:
        try:
            Posts.objects.get(pk=post_pk).delete()
            response = JsonResponse({'status':True,'success':'post deleted'})
            response.status_code = 201
            return response
        except Exception as e:
            response = JsonResponse({'status':False,'error':'Error post not deleted.Try again later'})
            response.status_code = 304
            return response
        
            
            
        


        

    
 
    
