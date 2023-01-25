#!/usr/bin/env python3
'''This module provides pagination functionality
'''
def index_range(page : int, page_size : int) ->tuple[int, int]:
    '''This function returns the first and last index of a page
    '''
    return (page * page_size, (page + 1) * page_size)
