"""
Module to hold queries to GraphQL PokeAPI v1beta
"""
from sgqlc.operation import Operation
from .schema import pokeapiv1beta_schema as pokeapi
from .connection import endpoint

def execute_operation(func):
    '''
    Decorator executor query
    '''
    def wrapper(*args, **kwargs):
        query = Operation(pokeapi.query_root)
        query = func(*args, **kwargs, query=query)
        result = endpoint(query=query)
        return result
    return wrapper

@execute_operation
def count_name_regex_match(regex_string, query=Operation(pokeapi.query_root)) -> Operation:
    """Return how many pokemon match with given regex in their name."""
    condition = {"name": {"_regex": regex_string}}
    match = query.pokemon_v2_pokemon_aggregate(where=condition)
    match.aggregate.count()
    return query

@execute_operation
def count_interbreed_species(name_pokemon, query=Operation(pokeapi.query_root)) -> Operation:
    """Return how many species can interbreed with given pokemon name."""
    condition = {
        "pokemon_v2_pokemonegggroups": {
            "pokemon_v2_egggroup": {
                "pokemon_v2_pokemonegggroups": {
                    "pokemon_v2_pokemonspecy": {
                        "pokemon_v2_pokemons": {"name": {"_eq": name_pokemon}}
                    }
                }
            }
        }
    }
    query.pokemon_v2_pokemonspecies_aggregate(where=condition).aggregate.count()
    return query

@execute_operation
def get_maxmin_weight_of_type_1gen(pokemon_type, query=Operation(pokeapi.query_root)) -> Operation:
    """Return max and min of given characteristic and type pokemon, 1st gen."""
    condition = {
        "_and": [
            {"id": {"_lte": 151}},
            {
                "pokemon_v2_pokemontypes": {
                    "pokemon_v2_type": {"name": {"_eq": pokemon_type}}
                }
            },
        ]
    }
    pokemons = query.pokemon_v2_pokemon_aggregate(where=condition)
    pokemons.aggregate.max.weight()
    pokemons.aggregate.min.weight()
    return query
