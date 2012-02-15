#!/usr/bin python
# encoding: utf-8

from math import sqrt, pow


def get_manhattan_distance(rating_left, rating_right):
    """
    tpye(rating) == dict
    """
    #    TODO
    count = 0
    total = 0
    for k in rating_left:
        if rating_right.has_key(k):
            count += 1
            total += abs(rating_left[k] - rating_right[k])
    if count != 0:
        return total / count
    else:
        return -1


def get_euclidean_distance(rating_left, rating_right):
#    TODO
    pass

