"""
Module of utilities
"""


def get_last_value_on_nested_dicts(dictionary):
    """Return deepest value different of type dict"""
    if isinstance(dictionary, dict):
        items = list(dictionary.items())
        if len(items) > 0 and isinstance(items[-1][1], dict):
            return get_last_value_on_nested_dicts(items[-1][1])
        return items[0][1]
    return dictionary


def get_two_deepest_values_on_nested_dicts(dictionary):
    """Return left and right values of nested dict with more than one item"""
    if isinstance(dictionary, dict):
        items = list(dictionary.items())
        if len(items) >= 2:
            left = get_last_value_on_nested_dicts({items[0][0]: items[0][1]})
            right = get_last_value_on_nested_dicts({items[-1][0]: items[-1][1]})
            return (left, right)
        else:
            return get_two_deepest_values_on_nested_dicts(items[0][1])
    return dictionary
