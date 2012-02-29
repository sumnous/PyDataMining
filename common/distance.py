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

def get_mean_value(input_list = []):
    """suggest that input_list is not null"""
    total = 0
    for x in input_list:
        total += float(x)
    return total/len(input_list)

def get_standard_deviation(input_list = []):
    total = 0
    num = len(input_list)
    mean_value = 0
#    print num
    result = -1
    if num:
        mean_value = get_mean_value(input_list)
#        print mean_value
        sum_deviation2 = 0 #means sum((xi - mean_value)^2)
        for x in input_list:
            sum_deviation2 += pow((x-mean_value),2)
#        print sum_deviation2

        result = sqrt(sum_deviation2/num)
    return result

def convert_values_normalization(origin_list = []):
    tag_list=[]
    input_list=[]

    for x in range(len(origin_list)):
        if origin_list[x] == None:
            tag_list.append(x)
        else:
            input_list.append(origin_list[x])

    std_deviation = get_standard_deviation(input_list)

    result = []
    num = len(input_list)

    if num:
        mean_value = get_mean_value(input_list)
        for x in input_list:
          result.append(float(x - mean_value)/float(std_deviation))

    for position in tag_list:
        result.insert(position,None)
        
    return result

#test
#print get_standard_deviation(origin_list=[1,2,4,5,8])
#print convert_values_normalization(origin_list=[1,2,4,None,5,8])

