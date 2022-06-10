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
        ('FLY','Flying'),
        ('FAI','Fairy')
    ]
    type = models.CharField(max_length=3,choices=TYPE_CHOICES)
    resistances = models.ManyToManyField(to="self",blank=True,symmetrical=False,related_name='resistance_set')
    immunities = models.ManyToManyField(to="self",blank=True,symmetrical=False,related_name='immunities_set')
    weaknesses = models.ManyToManyField(to="self",blank=True,symmetrical=False,related_name='weaknesses_set')

    def __str__(self):
        return self.type