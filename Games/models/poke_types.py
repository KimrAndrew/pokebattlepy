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

    def __repr__(self) -> str:
        return (
            f"""
            name: {self.name}
            resistances: {self.resistances}
            immunities: {self.immunities}
            weaknesses: {self.weaknesses}
            """
        )