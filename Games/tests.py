from django.test import TestCase
from Games.models.pokemon import Pokemon

# Create your tests here.
class PokemonTestCase(TestCase):
    def test_poke(self):
        bulbasaur = Pokemon.objects.create(id=1)
        bulbasaur.init()
