# Generated by Django 4.0.1 on 2022-06-16 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Games', '0016_pokemon_speed'),
    ]

    operations = [
        migrations.CreateModel(
            name='PokeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('FIR', 'Fire'), ('GRS', 'Grass'), ('WTR', 'Water'), ('BUG', 'Bug'), ('NRM', 'Normal'), ('PSN', 'Poison'), ('ELC', 'Electric'), ('GRD', 'Ground'), ('FGT', 'Fighting'), ('PSY', 'Psychic'), ('RCK', 'Rock'), ('GHT', 'Ghost'), ('ICE', 'Ice'), ('DRG', 'Dragon'), ('DRK', 'Dark'), ('STL', 'Steel'), ('FLY', 'Flying'), ('FAI', 'Fairy')], max_length=3)),
                ('immunities', models.ManyToManyField(blank=True, related_name='immunities_set', to='Games.PokeType')),
                ('resistances', models.ManyToManyField(blank=True, related_name='resistance_set', to='Games.PokeType')),
                ('weaknesses', models.ManyToManyField(blank=True, related_name='weaknesses_set', to='Games.PokeType')),
            ],
        ),
        migrations.DeleteModel(
            name='Type',
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='types',
            field=models.ManyToManyField(blank=True, to='Games.PokeType'),
        ),
    ]
