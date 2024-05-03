from django.contrib import admin
from tinkerhub_tinkercade.games.models import Games
# Register your models here.
@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "points",
    ]