# Generated by Django 4.0.1 on 2022-02-06 23:03

import Users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0022_trainer_cards_trainer_decks_trainer_prev_battles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='cards',
            field=models.JSONField(default=Users.models.init_cards),
        ),
    ]
