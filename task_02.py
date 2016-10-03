#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 06 synthesizing task_02"""

def prepare_email(appointments):
    """Remind clients about their appointments by sending an email.

    Args:
        Appointments(list): clients name and appointment in tuples.

    Returns:
        List: Displays a new list with each client's email body containing their name
              and appintment.

    Examples:
        >>> prepare_email([('Jen', '2015'), ('Max', 'March 3')]
        ['Dear Jen,\nI look forward to meeting with you on 2015.\nBest,\nMe',
        'Dear Max,\nI look forward to meeting you on March 3.\nBest\nMe']
        
    """
    email = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'
    nlist = []
    for list_item in appointments:
        name = list_item[0]
        date = list_item[1]
        nlist.append(email.format(name, date))

    return nlist
