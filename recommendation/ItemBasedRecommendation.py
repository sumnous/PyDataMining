#!/usr/bin python
# encoding: utf-8

from Recommendation import Recommendation

class ItemBasedRecommendation(Recommendation):
#    def __init__(self, user_rating={}, neighbor=3, recommendation=3):
#        pass
    def get_all_items(self):
        return self.user_rating.itervalues()

    def use_standard_user_rating(self):
        """
        在标准化的data里，0和没有评分很难区分。
        没有评分暂时用None表示
        """
        pass

        

if __name__ == '__main__':
    pass