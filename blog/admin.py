from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from blog.models import Blog, BlogMedia

class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogMedia)
