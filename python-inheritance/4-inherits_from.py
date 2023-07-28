#!/usr/bin/python3
"""A funciotn doing a bunch of stuff"""


def inherits_from(obj, a_class):
    """ A function using issubclass"""
    return issubclass(obj, a_class) and type(obj) != a_class
