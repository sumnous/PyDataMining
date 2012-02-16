#!/usr/bin python
# encoding: utf-8

from common import Martrix
from common.distance import get_manhattan_distance
from math import sqrt,pow
from conf import conf

class Recommendation(object):
    def __init__(self,neighbor = 3,recommendation = 3, user_rating_dict={}, training=False):
        self.n = neighbor #num
        self.r = recommendation #num

        self.save_type = conf.save_type
        self.cal_type = conf.cal_distance_type
        self.pearson_type = conf.pearson_cal_type

        if not training:
            if self.save_type == "Pickle":
                import pickle
                with file('../inter_data/user_items_rating.dict') as f:
                    self.user_rating = pickle.load(f)
        else:
            self.user_rating = user_rating_dict

    def load_configuration(self,fobject=None):
        """load configuration XML file"""

    def get_active_users(self):
        result = []
        # if number of items from one user > 3, consider as active user
        all_users = self.get_all_users()
        for x in all_users:
            if len(self.user_rating[x]) > conf.active_count:
                result.append(x)
        return  result

    def get_all_users(self):
        users = set(self.user_rating.iterkeys())
        return list(users)

    def get_all_items(self):
#        TODO
        return []


if __name__ == '__main__':
    pass