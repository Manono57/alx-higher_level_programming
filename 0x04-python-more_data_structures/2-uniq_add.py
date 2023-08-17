#!/usr/bin/python3

#elm is element

def uniq_add(my_list=[]):
    number = 0
    for elm in set(my_list):
        number += elm
    return number
