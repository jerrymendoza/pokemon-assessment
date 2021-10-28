"""
Tests queries required
"""

from graph.queries import count_name_regex_match, count_interbreed_species


def test_count_pokemon_name_regex():
    """Test count pokemon with 'ito' in their names
    [politoed, spiritomb, palpitoad, seismitoad]
    """
    expected = {"data": {"pokemon_v2_pokemon_aggregate": {"aggregate": {"count": 4}}}}
    assert count_name_regex_match(".*ito.*") == expected


def test_count_interbreed():
    """Test count species can interbreed with ditto"""
    expected = {
        "data": {"pokemon_v2_pokemonspecies_aggregate": {"aggregate": {"count": 1}}}
    }
    assert count_interbreed_species("ditto") == expected
