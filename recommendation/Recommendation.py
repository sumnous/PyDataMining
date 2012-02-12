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

    def get_all_users(self):
        return [x for x in self.users]

    def load_configuration(self,fobject=None):
        """load configuration XML file"""

    def get_nearest_neighbor(self,user):
        """return user list"""
        users = self.users
        distance = []
        for x in users:
            if user != x:
                d = get_manhattan_distance(users[user],users[x])
                distance.append((x,d))

        if len(distance) >= self.n:
            distance.sort()
            return [ x[0] for x in distance[:self.n]]
        elif len(distance) > 0 and len(distance) < self.n:
            distance.sort()
            return [ x[0] for x in distance]
        else :
            return distance

    def get_neighbor_recommendation_list(self,user,neighbors=[]):
    #        TODO
    #        prefer user or high score?
    #        item_neighbor_count = {}

        rec_dict = {}
        for x in neighbors:
            for item in self.users[x]:
                if not self.users[user].has_key(item):
                    if rec_dict.has_key(item):
                        rec_dict[item][x] = self.users[x][item]
                    else:
                        tmp = {}
                        tmp[x] = self.users[x][item]
                        rec_dict[item] = tmp

        rec_list = []
        for x in rec_dict:
            pearson_total = 0
            tmp_users = []
            for k in rec_dict[x]:
                tmp_users.append(k)

            pearson_list = self.get_pearson_value_list(user,users = tmp_users)
            for m in pearson_list:
                pearson_total += m[1]

            score = 0
            for record in pearson_list:
                score += (record[1]/pearson_total)*rec_dict[x][record[0]]
                #            print score
            rec_list.append((x,score))

        rec_list.sort(key=lambda d:d[1],reverse=True)

        return rec_list

    def get_pearson_value_list(self,user,users = []):
        values = []
        if len(users) == 0:
            return values
        else:
            from common.pearson import get_pearson_value as get_value
            for x in users:
                values.append((x,get_value(self.users[user],self.users[x])))
                #                print (x,get_value(self.users[user],self.users[x]))
            return values

    def cal_user_distance(self):
        """return Martrix"""
        users = self.users
        values = Martrix(0,0)

        if self.cal_type == "manhattan":
            if len(users) < 2:
                return values
            else:
                for left in users:
                    for right in users:
                    #TODO
                        pass
        else: #E distance
            pass



if __name__ == '__main__':
    from data_format.input_format import user_install_record_to_dict
    user_dict = user_install_record_to_dict(file('../input/user_usetimes_record.tmp'))
    rec = Recommendation(neighbor=5, user_rating = user_dict)

    #print "all-user"
    #print rec.get_all_users()
    #print rec.get_pearson_value_list(user='000000011234564', users = rec.get_nearest_neighbor(user='000000011234564'))
    
#    print rec.get_nearest_neighbor(user='000000011234564')
    print rec.get_neighbor_recommendation_list(user='000000011234564',neighbors=rec.get_nearest_neighbor(user='000000011234564'))




        
