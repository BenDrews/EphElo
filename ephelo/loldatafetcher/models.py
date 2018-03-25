from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class GameData(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    timestamp = models.DateTimeField('game date')
    tournament_code = models.CharField(max_length = None)
    json = models.CharField('match v2.0 data', max_length = None)
    # Participant Foreign Key

    def __str__(self):
        return self.json

class Participant(models.Model):
    game_data = models.ForeignKey(GameData, on_delete = models.CASCADE)
    profile = models.ForeignKey(Profile)
    championId = models.IntegerField()
    lane = models.CharField(max_length = 200)
    pick_order = models.CharField(max_length = 200)

    def __str__(self):
        return self.profile.summoner_name

class Profile(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    summoner_name = models.CharField(max_length = 200)
    summoner_id = models.IntegerField()
    # Elo Foreign Key
    # Participant Foreign Key

    def __str__(self):
        return self.summoner_name

class Elo(models.Model):
    models.ForeignKey(Profile, on_delete = models.CASCADE)
    timestamp = models.DateTimeField()
    elo = models.IntegerField()

    def __str__(self):
        pass
