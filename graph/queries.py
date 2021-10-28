"""
Module to hold queries to GraphQL PokeAPI v1beta
"""
from sgqlc.operation import Operation
from .schema import pokeapiv1beta_schema as pokeapi
from .connection import endpoint


def count_name_regex_match(regex_string) -> dict:
    """Return how many pokemon match with given regex in their name."""
    query = Operation(pokeapi.query_root)
    condition = {"name": {"_regex": regex_string}}
    match = query.pokemon_v2_pokemon_aggregate(where=condition)
    match.aggregate.count()
    result = endpoint(query=query)
    return result

def count_interbreed_species(name_pokemon) -> dict:
    """Return how many species can interbreed with given pokemon name."""
    query = Operation(pokeapi.query_root)
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
    result = endpoint(query=query)
    return result