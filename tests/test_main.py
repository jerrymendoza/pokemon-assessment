'''
Tests assessment answers
'''
from main import count_names_at_and_2a, n_interbreed_species_raichu, max_min_weight_1st_gen


def test_count_names_at_and_2a():
    ''' Check Answer to question 1 '''
    assert count_names_at_and_2a() == 24

def test_type_count_names_at_and_2a():
    ''' Check Type Answer to question 1 '''
    assert isinstance(count_names_at_and_2a(), int)

def test_n_interbreed_species_raichu():
    ''' Check Answer to question 2 '''
    assert  n_interbreed_species_raichu() == 258

def test_type_n_interbreed_species_raichu():
    ''' Check Type Answer to question 1 '''
    assert isinstance(n_interbreed_species_raichu(), int)

def test_max_min_weight_1st_gen():
    ''' Check Answer to question 3 '''
    assert max_min_weight_1st_gen() == [1300, 195]

def test_type_max_min_weight_1st_gen():
    ''' Check Type Answer to question 1 '''
    assert isinstance(max_min_weight_1st_gen(), list)

def test_length_max_min_weight_1st_gen():
    ''' Check Length Answer to question 1 '''
    assert len(max_min_weight_1st_gen()) == 2