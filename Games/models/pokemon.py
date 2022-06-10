from django.db import models
from Games.models.types import Type
class Pokemon(models.Model):
    name = models.CharField(max_length=32)
    attack = models.IntegerField()
    special_attack = models.IntegerField()
    defense = models.IntegerField()
    special_defense = models.IntegerField()
    types = models.ManyToManyField(to=Type)



