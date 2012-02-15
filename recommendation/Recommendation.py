#!/usr/bin python
# encoding: utf-8

from common import Martrix
from common.distance import get_manhattan_distance

from math import sqrt,pow

class Recommendation(object):
    def __init__(self,user_rating = {},neighbor = 3,recommendation = 3):
        self.n = neighbor #num
        self.r = recommendation #num
        self.cal_type = "manhattan"  # M/O
        self.pearson_type = "formula" #formula/normal/cosine
        self.users = user_rating

    def load_configuration(self,fobject=None):
        """load configuration XML file"""

    def get_all_users(self):
        return [x for x in self.users]
    def get_all_items(self):
        pass



if __name__ == '__main__':
    pass