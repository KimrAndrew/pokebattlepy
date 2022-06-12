from django.db import models
from Games.models.types import Type

import random
import pokebase

class Pokemon(models.Model):
    name = models.CharField(max_length=32,blank=True)
    attack = models.IntegerField(null=True)
    special_attack = models.IntegerField(null=True)
    defense = models.IntegerField(null=True)
    special_defense = models.IntegerField(null=True)
    types = models.ManyToManyField(blank=True,to=Type)
    official_artwork = models.SlugField(blank=True)
    front_sprite = models.SlugField(blank=True)
    back_sprite = models.SlugField(blank=True)

    def create(self):
        #pokemon = Pokemon.objects.filter(id=self.id)
        pokebase_req = pokebase.pokemon(self.id)
        print(pokebase_req)



