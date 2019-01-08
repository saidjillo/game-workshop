from django.contrib import admin

from game.models import Game, Ratings

# Register your models here.
class GameModelAdmin(admin.ModelAdmin):
    list_display = ['title','description']


admin.site.register(Game, GameModelAdmin)
admin.site.register(Ratings)
