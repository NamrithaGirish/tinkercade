from django.db import models

from tinkerhub_tinkercade.users.models import User
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

class Games(models.Model):
    name = models.CharField(max_length=14, unique=True)
    desc = models.CharField(max_length=200)
    points = models.IntegerField(default=10, null=True, blank=True)
    slug = models.SlugField(max_length=50, unique=True, editable=False)
    class Levels(models.TextChoices):
        LEVEL1 = "L1", _("Level-1")
        LEVEL2 = "L2", _("Level-2")
        LEVEL3 = "L3", _("Level-3")
    level = models.CharField(max_length=3, choices=Levels.choices,default=Levels.LEVEL1)
    quiz_link = models.URLField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name).upper()
        
        return super(Games, self).save(*args, **kwargs)


class UserGames(models.Model):
    id = models.CharField(max_length=100, default="TINKERCADE", primary_key=True)
    player = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="player"
    )
    games = models.ForeignKey(Games, on_delete=models.CASCADE)
    winning_points = models.IntegerField(default=0, null=True, blank=True)
    
    def __str__(self):
        return self.id

    @staticmethod
    def create_random_id():
        return random.randrange(1000, 9999)

    def save(self, *args, **kwargs):
        if not self.id:
            temp_id = f"TINKERCADE-{self.game.name.split()[0]}-{UserGames.create_random_id()}"
            while UserGames.objects.filter(id=temp_id).first():
                temp_id = (
                    f"TINKERCADE-{self.game.name.split()[0]}-{UserGames.create_random_id()}"
                )
            # self.slug = temp_id.upper()
            self.id = temp_id.upper()
        return super(UserGames, self).save(*args, **kwargs)
    

