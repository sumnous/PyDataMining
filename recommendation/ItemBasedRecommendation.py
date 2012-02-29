#!/usr/bin python
# encoding: utf-8

from Recommendation import Recommendation
from common.distance import convert_values_normalization

class ItemBasedRecommendation(Recommendation):
#    def __init__(self, user_rating={}, neighbor=3, recommendation=3):
#        pass

    def use_standard_user_rating(self, item_list=[]):
        """
        在标准化的data里，0和没有评分很难区分。
        没有评分暂时用None表示
        """
#        get standard value
        all_user = self.get_all_users()
        for x in item_list:
            input_list = []
            for u in all_user:
                if not self.user_rating[u].has_key(x):
                    input_list.append(None)
                else:
                    input_list.append(self.user_rating[u][x])
            normal_value = convert_values_normalization(input_list)
#            update value
            for i in len(normal_value):
                if normal_value[i] != None:
                    self.user_rating[all_user[i]][x] = normal_value[i]

        print "Use standard user rating."

if __name__ == '__main__':
    from data_format.input_format import user_install_record_to_dict

    flag = False
    user_dict = user_install_record_to_dict(file('../input/ml-100k/u.data'), training=flag)
    rec = ItemBasedRecommendation(neighbor=5, user_rating_dict=user_dict, training=flag)
#    print rec.get_all_users()
    print len(rec.get_all_items(user='123'))

    
#    ibr.use_standard_user_rating()
#    print ibr.user_rating
#    pass