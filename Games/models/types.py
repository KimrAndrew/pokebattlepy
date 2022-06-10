from django.db import models

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