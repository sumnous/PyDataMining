#!/usr/bin python
# encoding: utf-8

from common import Martrix, distance
from common.distance import get_manhattan_distance
from Recommendation import Recommendation

from math import sqrt, pow

class UserBasedRecommendation(Recommendation):
#    def __init__(self, neighbor=3, recommendation=3, training=False):

    def get_relative_neighbor(self, search_deep=1):
        pass
#        TODO
#        add method to find neighbor and may be relative user via neighbor.
    
    def get_nearest_neighbor(self, user, training=False, active_user_filter=False):
#        TODO
# add active_neighbor option. could return nearest neighbors and all of them are in active users set.
        """return user list"""
        users = self.user_rating
        distance = []
        for x in users:
            if user != x:
                d = get_manhattan_distance(users[user], users[x])
                distance.append((x, d))

        if len(distance) >= self.n:
            distance.sort()
            distance = [x[0] for x in distance[:self.n]]
        elif len(distance) > 0 and len(distance) < self.n:
            distance.sort()
            distance = [x[0] for x in distance]

        if training and self.save_type == "Pickle":
            import pickle
            with file('../inter_data/nearest_neighbor', 'w') as f:
                pickle.dump(distance, f)
                
        return distance

    def get_neighbor_recommendation_list(self, user, neighbors=[]):
    #        TODO
    #        prefer user or high score?
    #        item_neighbor_count = {}

        rec_dict = {}
        for x in neighbors:
            for item in self.user_rating[x]:
                if not self.user_rating[user].has_key(item):
                    if rec_dict.has_key(item):
                        rec_dict[item][x] = self.user_rating[x][item]
                    else:
                        tmp = {}
                        tmp[x] = self.user_rating[x][item]
                        rec_dict[item] = tmp

        rec_list = []
        for x in rec_dict:
            pearson_total = 0
            tmp_users = []
            for k in rec_dict[x]:
                tmp_users.append(k)

            pearson_list = self.get_pearson_value_list(user, users=tmp_users)
            for m in pearson_list:
                pearson_total += m[1]

            score = 0
            for record in pearson_list:
                if pearson_total !=0:
                    score += (record[1] / pearson_total) * rec_dict[x][record[0]]
                    #            print score
            rec_list.append((x, score))

        rec_list.sort(key=lambda d:d[1], reverse=True)

        return rec_list

    def get_pearson_value_list(self, user, users=[], training=False):
        values = []
        if len(users) != 0:
            from common.pearson import get_pearson_value as get_value
            for x in users:
                values.append((x, get_value(self.user_rating[user], self.user_rating[x])))
                #print (x,get_value(self.users[user],self.users[x]))
        if training and self.save_type == "Pickle":
            import pickle
            with file('../inter_data/pearson_value_list','w') as f:
                pickle.dump(values, f)
        return values

#    def cal_user_distance(self):
#        """return Martrix"""
#        users = self.users
#        values = Martrix(0, 0)
#
#        if self.cal_type == "manhattan":
#            if len(users) < 2:
#                return values
#            else:
#                for left in users:
#                    for right in users:
#                    #TODO
#                        pass
#        else: #E distance
#            pass


if __name__ == '__main__':

#   -----Training Part-----
    flag = True

    from data_format.input_format import user_install_record_to_dict

    user_dict = user_install_record_to_dict(file('../input/ml-100k/u.data'), training=flag)
    #    print user_dict
    rec = UserBasedRecommendation(neighbor=5, user_rating_dict=user_dict, training=flag)
#    print rec.get_all_users()
#    print rec.get_active_users()

#    one_user = rec.get_all_users()[0]
    one_user = '1'
#    for one_user in rec.get_all_users()[1:1]:
#    print user_dict['216']
#    nearest_neighbor = rec.get_nearest_neighbor(user=one_user, training=flag)
    nearest_neighbor = rec.get_active_users()
    pearson_value_list = rec.get_pearson_value_list(user=one_user, users=nearest_neighbor, training=flag)
#        print pearson_value_list
#        print rec.get_nearest_neighbor(user=one_user)
    for x in rec.get_neighbor_recommendation_list(user=one_user, neighbors = nearest_neighbor)[:20]:
        print x




        
