'''
Module of utilities
'''
def get_last_value_on_nested_dicts(dictionary):
    '''Return deepest value different of type dict
    '''
    items = list(dictionary.items())
    if len(items) > 0 and isinstance(items[-1][1], dict):
        return get_last_value_on_nested_dicts(items[-1][1])
    return items[0][1]
