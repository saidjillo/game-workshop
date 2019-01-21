from django.db import models

from django.utils import timezone
from django.template.defaultfilters import slugify

from gamelist.models import GameList

# Create your models here.
class Game(models.Model):
    title          = models.CharField(max_length=251)
    description    = models.TextField()
    game_developer = models.CharField(max_length=150)
    url            = models.URLField()
    image_cover    = models.ImageField(upload_to="images/%Y/%m/%d")
    date_uploaded  = models.DateTimeField(default=timezone.now)
    slug           = models.SlugField()
    views          = models.IntegerField(default=0)
    game_list      = models.ForeignKey(GameList, on_delete=models.CASCADE, related_name="game")

    def slug(self):
        return slugify(self.title)

    def __str__(self):
        return self.title

    def get_name(self):
        return __class__.__name__


class HitCount(models.Model):
    game      = models.ForeignKey(Game, related_name="hitcounts", on_delete=models.CASCADE)
    hits      = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.game.title

    def increase_hit(self):
        self.hits += 1
        self.save()



class Ratings(models.Model):
    stars  = models.IntegerField()
    game   = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="stars")

    def __str__(self):
        return f'{self.game.title} stars => {self.stars}'