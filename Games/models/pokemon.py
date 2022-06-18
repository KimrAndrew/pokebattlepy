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
    

    @classmethod
    def create(cls,id):
        #Initialize Pokemon
        pokemon = Pokemon(id=id)
        pokemon.save()

        #Make request to Pokebase API
        pokebase_req = pokebase.pokemon(pokemon.id)

        #Populate Pokemon Stats
        pokemon.name = pokebase_req.species.name
        print(f'Initializing Pokemon {pokemon.name}')
        pokemon.attack = pokebase_req.stats[1].base_stat
        pokemon.defense = pokebase_req.stats[2].base_stat
        pokemon.special_attack = pokebase_req.stats[3].base_stat
        pokemon.special_defense = pokebase_req.stats[4].base_stat

        #Add Pokemon Types
        poke_types = pokebase_req.types
        poke_types = [poke_type.type.name for poke_type in poke_types]
        print(f'Created Pokemon {pokemon.name} with stats:\n    Attack: {pokemon.attack}\n    Defense: {pokemon.defense}\n    Special Attack: {pokemon.special_attack}\n    Special Defense: {pokemon.special_defense}\n')
        for poke_type in poke_types:
            type_queryset = PokeType.objects.filter(name=poke_type)
            if len(type_queryset):
                print(f'{poke_type} found! Adding to Pokemon {pokemon.name}...')
                pokemon.types.add(type_queryset[0])
            else:
                print(f'{poke_type} not found.')
        print(f'Initialization for Pokemon: {pokemon.name} complete!')

        #Save Pokemon to DB and return
        pokemon.save()
        return pokemon


    def __str__(self):
        return self.name



