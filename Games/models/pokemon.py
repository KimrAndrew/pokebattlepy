from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=32)
    attack = models.IntegerField()
    special_attack = models.IntegerField()
    defense = models.IntegerField()
    special_defense = models.IntegerField()
    types = models.ManyToManyField(to=)

class Type(models.Model):
    TYPE_CHOICES = [
        ('FIR','Fire'),
        ('GRS','Grass'),
        ('WTR','Water'),
        ('BUG','Bug'),
        ('NRM','Normal'),
        ('PSN','Poison'),
        ('ELC','Electric'),
        ('GRD','Ground'),
        ('FGT','Fighting'),
        ('PSY','Psychic'),
        ('RCK','Rock'),
        ('GHT','Ghost'),
        ('ICE','Ice'),
        ('DRG','Dragon'),
        ('DRK','Dark'),
        ('STL','Steel'),
        ('FLY','Flying')
    ]
    type = models.CharField(max_length=3,choices=TYPE_CHOICES)

