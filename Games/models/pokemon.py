from django.db import models
from Games.models.poke_types import PokeType

import random
import pokebase

class Pokemon(models.Model):
    name = models.CharField(max_length=32,blank=True)
    attack = models.IntegerField(null=True)
    special_attack = models.IntegerField(null=True)
    defense = models.IntegerField(null=True)
    special_defense = models.IntegerField(null=True)
    speed = models.IntegerField(null=True)
    types = models.ManyToManyField(blank=True,to=PokeType)
    official_artwork = models.SlugField(blank=True)
    front_sprite = models.SlugField(blank=True)
    back_sprite = models.SlugField(blank=True)

    def init(self):
        #pokemon = Pokemon.objects.filter(id=self.id)
        pokebase_req = pokebase.pokemon(self.id)
        #print(pokebase_req)
        #print(pokebase_req.stats[0].stat.name)
        self.name = pokebase_req.species.name
        print(f'Initializing Pokemon {self.name}')
        self.attack = pokebase_req.stats[1].base_stat
        self.defense = pokebase_req.stats[2].base_stat
        self.special_attack = pokebase_req.stats[3].base_stat
        self.special_defense = pokebase_req.stats[4].base_stat

        poke_types = pokebase_req.types
        poke_types = [poke_type.type.name for poke_type in poke_types]
        print(f'Created Pokemon {self.name} with stats:\n    Attack: {self.attack}\n    Defense: {self.defense}\n    Special Attack: {self.special_attack}\n    Special Defense: {self.special_defense}\n')
        for poke_type in poke_types:
            type_queryset = PokeType.objects.filter(name=poke_type)
            if len(type_queryset):
                print(f'{poke_type} found! Adding to Pokemon {self.name}...')
                self.types.add(type_queryset[0])
            else:
                print(f'{poke_type} not found.')
        print(f'Initialization for Pokemon: {self.name} complete!')
            #self.types.add(PokeType.objects.filter(name=poke_type))
        
        # self.types.add(Type.objects.filter(type=pokebase_req.types[0].type.name)[0])



