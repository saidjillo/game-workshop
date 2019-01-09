from django.contrib import admin

from game.models import Game, Ratings, HitCount

# Register your models here.
class GameModelAdmin(admin.ModelAdmin):
    list_display = ['title','description']

class HitCountModelAdmin(admin.ModelAdmin):
    model  = HitCount
    list_display =  ['get_game', 'hits']

    def get_game(self, obj):
        return obj.game.title

    get_game.admin_order_field  = 'game'  #Allows column order sorting
    get_game.short_description = 'name of game'  #Renames column head


admin.site.register(Game, GameModelAdmin)
admin.site.register(Ratings)
admin.site.register(HitCount,HitCountModelAdmin)
