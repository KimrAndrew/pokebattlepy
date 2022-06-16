from django.db import models

class PokeType(models.Model):

    TYPE_CHOICES = [
        ('fire','Fire'),
        ('grass','Grass'),
        ('water','Water'),
        ('bug','Bug'),
        ('normal','Normal'),
        ('poison','Poison'),
        ('electric','Electric'),
        ('ground','Ground'),
        ('fighting','Fighting'),
        ('psychic','Psychic'),
        ('rock','Rock'),
        ('ghost','Ghost'),
        ('ice','Ice'),
        ('dragon','Dragon'),
        ('dark','Dark'),
        ('steel','Steel'),
        ('flying','Flying'),
        ('fairy','Fairy')
    ]

    name = models.CharField(max_length=16,choices=TYPE_CHOICES)
    resistances = models.ManyToManyField(to="self",blank=True,symmetrical=False,related_name='resistance_set')
    immunities = models.ManyToManyField(to="self",blank=True,symmetrical=False,related_name='immunities_set')
    weaknesses = models.ManyToManyField(to="self",blank=True,symmetrical=False,related_name='weaknesses_set')


    def __str__(self):
        return self.name

    # def _get_abbrev(self,type):
    #     types = {
    #         'Fire': 'FIR',
    #         'Grass': 'GRS',
    #         'Water': 'WTR',
    #         'Bug': 'BUG',
    #         'Normal': 'NRM',
    #     }