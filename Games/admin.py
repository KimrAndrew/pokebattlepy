from django.contrib import admin
from Games.models.game import Game
from Games.models.pokemon import Pokemon
from Games.models.poke_types import PokeType


admin.site.register((Game,PokeType,Pokemon))