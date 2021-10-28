"""
1. Obtén cuantos pokemones poseen en sus nombres “at” y tienen 2 “a” en su nombre, incluyendo la primera del “at”. 
    Tu respuesta debe ser un número.

2. ¿Con cuántas especies de pokémon puede procrear raichu? (2 Pokémon pueden procrear si están dentro del mismo egg group). 
    Tu respuesta debe ser un número. Recuerda eliminar los duplicados.

3. Entrega el máximo y mínimo peso de los pokémon de tipo fighting de primera generación (cuyo id sea menor o igual a 151). 
    Tu respuesta debe ser una lista con el siguiente formato: [1234, 12], en donde 1234 corresponde al máximo peso y 12 al mínimo.
"""

from graph.queries import (
    count_name_regex_match,
    count_interbreed_species,
    get_maxmin_weight_of_type_1gen,
)
import utils


def count_names_at_and_2a() -> int:
    """Count how many pokemon have "at" and two "a" in their name."""
    condition_regex_string = "(?=.*(at).*)(.*(a).*){2}"
    result = count_name_regex_match(condition_regex_string)
    return utils.get_last_value_on_nested_dicts(result)


def n_interbreed_species_raichu() -> int:
    """Cound how many species can interbreed with raichu"""
    result = count_interbreed_species("raichu")
    return utils.get_last_value_on_nested_dicts(result)


def max_min_weight_fighting_gen1() -> list[int]:
    """Get max and min weight of pokemon fighting type, 1st Gen only."""
    result = get_maxmin_weight_of_type_1gen('fighting')
    return list(utils.get_two_deepest_values_on_nested_dicts(result))
