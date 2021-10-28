'''
Tests utilities
'''
from utils import get_last_value_on_nested_dicts

def test_deepest_value():
    nested_dictionary = {'key':{'key2':{'key3':'value4'}}}
    expected = 'value4'
    assert get_last_value_on_nested_dicts(nested_dictionary) == expected
