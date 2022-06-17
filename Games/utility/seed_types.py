from Games.models.poke_types import PokeType
from GameLogic.type_table import type_table
#300 seconds run time -> 200 -> 173 -> 143
def seed_type_data(types):
    poke_type_models = {}
    for type in types:
        print(f'Initializing Type: {type}...')
        poke_type:PokeType = PokeType.objects.create(name=type)
        poke_type.save()
        # Builds up dictionary of poke_types. Using a dictionary saves on time consumimg DB calls
        poke_type_models[type] = poke_type


    print('\n')

    for type in types:
        print(f'Adding information for Type: {type}...')
        type_data:dict = types[type]
        
        for weakness in type_data['weaknesses']:
            print(f'    Adding {weakness} to {poke_type_models[type]} weaknesses...')
            poke_type_models[type].weaknesses.add(poke_type_models[weakness])

        for resistance in type_data['resistances']:
            print(f'    Adding {resistance} to {poke_type_models[type]} resistances...')
            poke_type_models[type].resistances.add(poke_type_models[resistance])

        for immunity in type_data['immunities']:
            print(f'    Adding {immunity} to {poke_type_models[type]} immunities...')
            poke_type_models[type].immunities.add(poke_type_models[immunity])

        poke_type_models[type].save()
        print(f'    Data for Type: {type} added successfully!\n')
        

if __name__ == '__main__':
    seed_type_data(type_table)