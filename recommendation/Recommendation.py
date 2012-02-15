#!/usr/bin python
# encoding: utf-8

from common import Martrix
from common.distance import get_manhattan_distance
from math import sqrt,pow

class Recommendation(object):
    def __init__(self,neighbor = 3,recommendation = 3, user_rating_dict={}, training=False):
        self.n = neighbor #num
        self.r = recommendation #num

        #        -----Need move into config.xml-----
        #
        #-----Config-----
        #need move into config.xml
        self.save_type = "Pickle"
        #

        self.cal_type = "manhattan"  # M/O
        self.pearson_type = "formula" #formula/normal/cosine

        if not training:
            if self.save_type == "Pickle":
                import pickle
                with file('../inter_data/user_items_rating.dict') as f:
                    self.user_rating = pickle.load(f)
        else:
            self.user_rating = user_rating_dict

    def load_configuration(self,fobject=None):
        """load configuration XML file"""

    def get_all_users(self):
        users = set([x for x in self.user_rating])
        return list(users)

    def get_all_items(self):
#        TODO
        return []

if __name__ == '__main__':
    pass