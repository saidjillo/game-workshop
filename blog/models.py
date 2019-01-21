from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title   = models.CharField(max_length=255)
    content = models.TextField()
    views   = models.IntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    writer  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    image   = models.ImageField(upload_to="blogs/%Y/%m/%d")
    slug    = models.SlugField(unique=True)

    def slug(self):
        return slugify(self.title)

    def __str__(self):
        return self.title

    def get_name(self):
        return __class__.__name__

class BlogMedia(models.Model):
    blog  = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='medias')
    image_one = models.ImageField(upload_to="blogs/%Y/%m/%d")
    image_two = models.ImageField(upload_to="blogs/%Y/%m/%d")
    image_three = models.ImageField(upload_to="blogs/%Y/%m/%d")

    def __str__(self):
        return self.blog.title