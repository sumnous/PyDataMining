__author__ = 'Administrator'

#!/usr/bin python
#encoding: utf-8

from distance import get_mean_value

deviations_like = {}
frequencies_like = {}
deviations_dislike = {}
frequencies_dislike = {}

def get_deviation(users):
    deviations = {}
    frequencies = {}
    #for each person in the data:
    #    get their ratings
    for ratings in users.values():
        #for each item & rating in that set of ratings:
        for (item, rating) in ratings.items():
            if rating == {}:
                break
            frequencies.setdefault(item, {})
            deviations.setdefault(item, {})
            #for each item_inner & rating_inner in that set of ratings:
            for (item_inner, rating_inner) in ratings.items():
                if rating_inner == {}:
                    break
                if item != item_inner:
                #add the difference between the ratings to our computation
                    frequencies[item].setdefault(item_inner, 0)
                    deviations[item].setdefault(item_inner, 0.0)
                    frequencies[item][item_inner] += 1
                    deviations[item][item_inner] += (rating - rating_inner)
    for (item, ratings) in deviations.items():
        for item_inner in ratings:
            ratings[item_inner] /= frequencies[item][item_inner]
    return deviations, frequencies

def get_deviation_likePolar(users):
    #for each person in the data:
    #    get their ratings
    global deviations_like
    global frequencies_like
    global deviations_dislike
    global frequencies_dislike
    u_mean = 0
    import copy
    users_like = copy.deepcopy(users)
    users_dislike = copy.deepcopy(users)
    # compute the u_mean
    for key in users.keys():
        u_mean = get_mean_value(users[key].values())
    print u_mean

    for k in users.keys():
        for item in users[k]:
            deviations_like.setdefault(item, {})
            frequencies_like.setdefault(item, {})
            deviations_dislike.setdefault(item, {})
            frequencies_dislike.setdefault(item, {})
            # get users_like dic
            if users_like[k][item] > u_mean:
                pass
            else:
                users_like[k][item] = {}
            # get users_dislike dic
            if users_dislike[k][item] < u_mean:
                pass
            else:
                users_dislike[k][item] = {}
    # computer the deviations
    #print "users_like: ", users_like
    #print "users_dislike: ", users_dislike
    (deviations_like, frequencies_like) = get_deviation(users_like)
    (deviations_dislike, frequencies_dislike) = get_deviation(users_dislike)
    return [deviations_like, frequencies_like, deviations_dislike, frequencies_dislike]

def slopeOne_biPolar_recommendations(userRatings):
    """
    This algorithm is consider the two items' similarity is effected by both of
    the like part of users ratings and the dislike part.
    """
    recommendations = {}
    frequencies4s1 = {}
    tem1_rec = {}
    tem1_fre = {}
    tem2_rec = {}
    tem2_fre = {}

    # for every item and rating in the user's recommendations
    for (userItem, userRating) in userRatings.items():
        # for every item in our users_like dataset that the user didn't rate
        for (diffItem_like, diffRatings_like) in deviations_like.items():
            if diffItem_like not in userRatings and userItem in deviations_like[diffItem_like]:
                freq_like = frequencies_like[diffItem_like][userItem]
                tem1_rec.setdefault(diffItem_like, 0.0)
                tem1_fre.setdefault(diffItem_like, 0)
                # add to the running sum representing the numerator of the formula
                tem1_rec[diffItem_like] += ((diffRatings_like[userItem] + userRating) * freq_like)
                import copy
                recommendations = copy.deepcopy(tem1_rec)
                # keep a running sum of the frequency of diffItem
                tem1_fre[diffItem_like] += freq_like
                frequencies4s1 = copy.deepcopy(tem1_fre)
        # for every item in our users_dislike dataset that the user didn't rate
        for (diffItem_dislike, diffRatings_dislike) in deviations_dislike.items():
            if diffItem_dislike not in userRatings and userItem in deviations_dislike[diffItem_dislike]:
                freq_dislike = frequencies_dislike[diffItem_dislike][userItem]
                tem2_rec.setdefault(diffItem_dislike, 0.0)
                tem2_fre.setdefault(diffItem_dislike, 0)
                # add to the running sum representing the numerator of the formula
                tem2_rec[diffItem_dislike] += ((diffRatings_dislike[userItem] + userRating) * freq_dislike)
                # keep a running sum of the frequency of diffItem
                tem2_fre[diffItem_dislike] += freq_dislike
    recommendations = dict(recommendations, **tem2_rec)
    frequencies4s1 = dict(frequencies4s1, **tem2_fre)
    recommendations = [(k, v / frequencies4s1[k]) for [k, v] in recommendations.items()]
    # finally sort and return
    recommendations.sort(key = lambda artistTuple: artistTuple[1], reverse = True)
    return recommendations

# test 02 using MovieLens DataSet
flag = True
from data_format.input_format import user_install_record_to_dict
user_dict = user_install_record_to_dict(file('C:/Program Files/Geany/RecSys_Python/ml-100k/ua.test'), training=flag)
get_deviation_likePolar(user_dict)
g = user_dict['1']
print "slopeone result: \n", slopeOne_biPolar_recommendations(g), "\n"