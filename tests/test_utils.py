'''
Tests utilities
'''
from utils import get_last_value_on_nested_dicts, get_two_deepest_values_on_nested_dicts

def test_deepest_value():
    nested_dictionary = {'key':{'key2':{'key3':'value4'}}}
    expected = 'value4'
    assert get_last_value_on_nested_dicts(nested_dictionary) == expected

def test_right_left_values():
    nested_dictionary = {'data': {'left_key':'left_value', 'center_key':'center_value' ,'right_key':'right_value'}}
    expected = ('left_value', 'right_value')
    assert get_two_deepest_values_on_nested_dicts(nested_dictionary) == expected