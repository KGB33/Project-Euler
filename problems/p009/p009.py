# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 01:13:41 2018

@author: kelton

Project Euler #9

Successful, triplets = [200,375,425]
"""

import numpy as np


def find_triplet():
    triplets = [1, 1, 1]
    print(triplets)
    triplets = incroment_triplets(triplets)
    print(triplets)


def incroment_triplets(arg):
    Condition1 = False
    if trip_sum(arg) == 1000:
        Condition2 = True
        if (
            np.sqrt(pow(arg[0], 2) + pow(arg[1], 2)) % 1 == 0
            and np.sqrt(pow(arg[0], 2) + pow(arg[1], 2)) == arg[2]
        ):
            Condition1 = True
            print("Testing powers")
        else:
            Condition1 = False
    else:
        Condition2 = False
    while Condition1 == False or Condition2 == False:
        print("In while loop, arg: ", arg)
        if arg[0] > arg[1]:
            arg[0] = 0
            arg[1] = arg[1] + 1
        else:
            arg[0] = arg[0] + 1
        arg[2] = 1000 - arg[1] - arg[0]
        print("While loop halfway point, arg: ", arg)

        if trip_sum(arg) == 1000:
            Condition2 = True
            if (
                np.sqrt(pow(arg[0], 2) + pow(arg[1], 2)) % 1 == 0
                and np.sqrt(pow(arg[0], 2) + pow(arg[1], 2)) == arg[2]
            ):
                Condition1 = True
                print("Testing powers")
            else:
                Condition1 = False
        else:
            Condition2 = False


def trip_sum(arg):
    arg_sum = arg[0] + arg[1] + arg[2]
    # print("This is trip Sum")
    return arg_sum


find_triplet()
