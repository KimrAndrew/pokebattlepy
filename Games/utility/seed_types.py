from Games.models.poke_types import PokeType
from GameLogic.type_table import type_table

def seed_type_data(types):
    for type in types:
        print(f'Initializing Type: {type}...')
        poke_type:PokeType = PokeType.objects.create(name=type)
        poke_type.save()

    print('\n')

    for type in types:
        print(f'Adding information for Type: {type}...')
        poke_type:PokeType = PokeType.objects.get(name=type)
        type_data:dict = types[type]

        for weakness in type_data['weaknesses']:
            print(f'    Adding {weakness} to {poke_type} weaknesses...')
            poke_type.weaknesses.add(PokeType.objects.get(name=weakness))

        for resistance in type_data['resistances']:
            print(f'    Adding {resistance} to {poke_type} resistances...')
            poke_type.resistances.add(PokeType.objects.get(name=resistance))

        for immunity in type_data['immunities']:
            print(f'    Adding {immunity} to {poke_type} immunities...')
            poke_type.immunities.add(PokeType.objects.get(name=immunity))

        poke_type.save()
        print(f'    Data for Type: {type} added successfully!\n')
        

if __name__ == '__main__':
    seed_type_data(type_table)