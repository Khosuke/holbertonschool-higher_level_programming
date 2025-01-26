#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    
    sum_weighted_score = 0
    sum_weight = 0
    for i in my_list:
        sum_weighted_score += (i[0] * i[1])
        sum_weight += i[1]
    average = sum_weighted_score / sum_weight
    return average
