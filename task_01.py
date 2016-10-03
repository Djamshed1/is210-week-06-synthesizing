#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 06 Synthesizing task"""

def get_party_stats(families, table_size=6):
    """This function counts the number of people and tables

    Args:
        families(nested list): the list of families and their members
        table_size(int): how much seats each table has
        
    Returns:
        Returns the total number of guests and and how many table needed
        
    Examples:
        >>> get_party_stats(['Jen', 'Jess'])
        (7, 2)

        >>> get_party_stats(['Jan'])
        (3, 1)
    """
    tables = 0
    guests = 0
    for obj in families:
        guests += len(obj)
        tables += -(-len(obj) // table_size)
        return (guests, tables)
