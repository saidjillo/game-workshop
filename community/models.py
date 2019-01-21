from django.db import models
from django.utils import timezone


from account.models import Member
from django.contrib.auth.models import User
from game.models import Game
from gamelist.models import GameList



# Create your models here.
class Forum(models.Model):
    game         = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='forums')
    date_created = models.DateTimeField(default=timezone.now)
    member       = models.ManyToManyField(Member, related_name='forums')
    forum_admin  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admins')
    topic        = models.CharField(max_length=2500, null=False, blank=False)

    def __str__(self):
        return self.topic

    def get_name(self):
        return __class__.__name__

class Posts(models.Model):
    forum       = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='posts')
    post_owner  = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='posts')
    date_posted = models.DateTimeField(default=timezone.now)
    post        = models.TextField()

    def __str__(self):
        return self.post


class ReplyToPost(models.Model):
    post         = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='replies')
    owner        = models.ForeignKey(Member,on_delete=models.CASCADE, related_name='replies')
    date_replied = models.DateTimeField(default=timezone.now)
    reply        = models.TextField()

    def __str__(self):
        return self.reply
