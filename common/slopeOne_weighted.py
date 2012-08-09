__author__ = 'Administrator'

#!/usr/bin python
#encoding: utf-8

from math import sqrt, pow

users2 = {"Amy": {"Dr. Dog": 4, "Lady Gaga": 3, "Phoenix": 4},
          "Ben": {"Dr. Dog": 5, "Lady Gaga": 2},
          "Clara": {"Lady Gaga": 3.5, "Phoenix": 4}}

deviations = {}
frequencies = {}

def get_deviation(users):
    #for each person in the data:
    #    get their ratings
    global deviations
    global frequencies
    for ratings in users.values():
        #for each item & rating in that set of ratings:
        for (item, rating) in ratings.items():
            frequencies.setdefault(item, {})
            deviations.setdefault(item, {})
            #for each item_inner & rating_inner in that set of ratings:
            for (item_inner, rating_inner) in ratings.items():
                if item != item_inner:
                #add the difference between the ratings to our computation
                    frequencies[item].setdefault(item_inner, 0)
                    deviations[item].setdefault(item_inner, 0.0)
                    frequencies[item][item_inner] += 1
                    deviations[item][item_inner] += rating - rating_inner
    for (item, ratings) in deviations.items():
        for item_inner in ratings:
            ratings[item_inner] /= frequencies[item][item_inner]
    return deviations, frequencies


def slopeOne_weighted_recommendations(userRatings):
    recommendations = {}
    frequencies4s1 = {}
    # for every item and rating in the user's recommendations
    for (userItem, userRating) in userRatings.items():
        # for every item in our dataset that the user didn't rate
        for (diffItem, diffRatings) in deviations.items():
            if diffItem not in userRatings and userItem in deviations[diffItem]:
                freq = frequencies[diffItem][userItem]
                recommendations.setdefault(diffItem, 0.0)
                frequencies4s1.setdefault(diffItem, 0)
                # add to the running sum representing the numerator of the formula
                recommendations[diffItem] += (diffRatings[userItem] + userRating) * freq
                # keep a running sum of the frequency of diffItem
                frequencies4s1[diffItem] += freq
    recommendations = [(k, v / frequencies4s1[k]) for [k, v] in recommendations.items()]
    # finally sort and return
    recommendations.sort(key = lambda artistTuple: artistTuple[1], reverse = True)
    return recommendations

# test 01 using users2 dic
print get_deviation(users2)
g = users2['Ben']
print slopeOne_weighted_recommendations(g)

# test 02 using MovieLens DataSet
flag = True
from data_format.input_format import user_install_record_to_dict
user_dict = user_install_record_to_dict(file('C:/Program Files/Geany/RecSys_Python/ml-100k/u.data'), training=flag)
get_deviation(user_dict)
g = user_dict['1']
print "slopeone result: \n", slopeOne_weighted_recommendations(g), "\n"


