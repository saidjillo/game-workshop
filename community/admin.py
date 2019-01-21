from django.contrib import admin

from community.models import Forum, Posts, ReplyToPost

# Register your models here.
admin.site.register(Forum)
admin.site.register(Posts)
admin.site.register(ReplyToPost)
