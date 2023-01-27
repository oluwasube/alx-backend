#!/usr/bin/python3
'''
Fifo dictionary
'''
from base_caching import BaseCaching

class FifoCache(BaseCaching):
    '''
    FIFO CACHEING
    '''
    def __init__(self):
        super().__init__()
        
    def put(self, key, item):
        '''
        Puts an item into the cache and discard last if cache_data is greater than max items
        '''
        if key is not None or item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(list(self.cache_data.keys())[-1]))
                del self.cache_data[list(self.cache_data.keys())[-1]]
            self.cache_data[key] = item

    def get(self, key):
        '''
        
        '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]