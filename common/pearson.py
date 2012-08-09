#!/usr/bin python
#encoding: utf-8

from math import sqrt, pow

""""calculate Pearson Correlation Coefficient"""

def get_pearson_value(rating_left, rating_right):
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    sum_y2 = 0
    count = 0
    for key in rating_left:
        if key in rating_right:
            count += 1
            x = rating_left[key]
            y = rating_right[key]
            sum_xy += x * y
            sum_x += x
            sum_y += y
            sum_x2 += pow(x, 2)
            sum_y2 += pow(y, 2)

    if count == 0:
    #        print "count == 0"
        return 0

    denominator = sqrt(sum_x2 - pow(sum_x, 2) / count) * sqrt(sum_y2 - pow(sum_y, 2) / count)
    if denominator == 0:
        return 0
    else:
        return (sum_xy - (sum_x * sum_y) / count) / denominator


def get_cosine_formula(rating_left, rating_right):
#    TODO
#    pass
    sum_x2 = 0
    sum_y2 = 0
    count = 0
    for key in rating_left:
        if key in rating_right:
            count += 1
            x = rating_left[key]
            y = rating_right[key]
            sum_x2 += pow(x, 2)
            sum_y2 += pow(y, 2)
    if count == 0:
        return 0
    else:
        return x * y / (sqrt(sum_x2) * sqrt(sum_y2))