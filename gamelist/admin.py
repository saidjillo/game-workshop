from django.contrib import admin

from gamelist.models import GameList

# Register your models here.
class GameListModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description','date_created','views','owner','slug']
    list_display_links = ['name', 'description']


admin.site.register(GameList, GameListModelAdmin)

