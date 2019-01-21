from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.


class Member(models.Model):

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('home', kwargs={'pk': self.pk})

    user =models.OneToOneField(User,related_name="member", on_delete=models.CASCADE)
    proffession = models.TextField(blank=True, null=True, default="works at gameworkshop")
    pic  = models.ImageField(upload_to="account/%Y/%m/%d", default="/account/image_placeholder.jpg")


def create_member(sender,**kwargs):
    if kwargs['created']:
        member = Member.objects.create(user=kwargs['instance'])

post_save.connect(create_member, sender=User)