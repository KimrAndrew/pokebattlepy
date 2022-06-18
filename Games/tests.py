from django.test import TestCase
from Games.models.pokemon import Pokemon
from Games.utility.seed_types import seed_type_data
from GameLogic.type_table import type_table

# Create your tests here.
class PokemonTestCase(TestCase):
    def setUp(self):
        print('Running setup for PokemonTestCase')
        seed_type_data(type_table)
    def test_poke(self):
        print('Method: test_poke')
        for id in range(1,5):
            poke = Pokemon.create(id=id)
            #poke.init()
            print(poke)
