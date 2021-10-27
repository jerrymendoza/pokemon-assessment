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
