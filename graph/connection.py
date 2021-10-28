'''
Build HTTP endpoint object
'''
from sgqlc.endpoint.http import HTTPEndpoint

_URL = 'https://beta.pokeapi.co/graphql/v1beta'
_HEADERS = {
    'User-Agent': """ Mozilla/5.0 (Macintosh;
                    Intel Mac OS X 10_15_4) AppleWebKit/537.36 
                    (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 """ }

def endpoint(*args,**kwargs):
    '''Return result of query execution'''
    return HTTPEndpoint(_URL, _HEADERS)(*args,**kwargs)
