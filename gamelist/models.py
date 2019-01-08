from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify

from account.models import Member

# Create your models here.
class GameList(models.Model):
    name        = models.CharField(max_length=500)
    description  = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    views        = models.IntegerField(default=0)
    owner        = models.ForeignKey(Member, on_delete=models.CASCADE)
    slug         = models.SlugField()


    def slug(self):
        return slugify(self.name)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('list:list_detail', kwargs={'pk': self.pk})
    
    def get_name(self):
        return __class__.__name__

    