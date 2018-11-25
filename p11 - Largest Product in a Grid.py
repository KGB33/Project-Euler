# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 13:39:47 2018

@author: kelto
"""

"""
Largest product in a grid
Problem 11 
In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction 
(up, down, left, right, or diagonally) in the 20×20 grid?
"""
from PrimeTools import timer
import time
import numpy as np # doesn't look like numpy is working w/ python 3.7


def main():
    maxes = {}
    
    # read in text
    with open("p11 - data.txt") as file:
        text_grid = file.read()
    
    # convert text to 2D array
    array = text_grid.split('\n')
    array = [i.split() for i in array]
    
    # convert strings in array to ints
    for row in array:
        for i in range(0, len(row)):
            row[i] = int(row[i])
    # print_array(array)

    # find max products
    maxes.update({"Max Diagonal": find_max_diagonal(array)})
    maxes.update({"Max Vertical": find_max_vertical(array)})
    maxes.update({"Max Horizontal": find_max_horizontal(array)})
    array = np.transpose(array) # transpose to get other half of array
    maxes.update({"Max T-Diagonal": find_max_diagonal(array)})

    # find the max of the maxes
    mega_max = find_max_in_dic(maxes)

    # print data
    print("\n\n\nMegaMax: {0}".format(mega_max))
    print_dic(maxes)


def find_max_horizontal(array):
    maximum = 0
    for row in array:
        for i in range(0, len(row)):
            product = 1
            try:
                # print(row)
                for s in range(0, 4):
                    # print(row[i + s])
                    product *= row[i + s]
            except IndexError:
                # print("index error in max horizontal")
                pass
            if product > maximum:
                maximum = product
    return maximum


def find_max_vertical(array):
    maximum = 0
    for r in range(0, len(array)):
        for c in range(0, len(array)):
            product = 1
            # print("R: {0}, C: {1}".format(r, c))
            try:
                for s in range(0, 4):
                    # print("\t{0}".format(array[r + s][c]))
                    product *= array[r + s][c]
            except IndexError:
                # print("Vert. Array Error")
                pass
            if product > maximum:
                maximum = product
    return maximum
                

def find_max_diagonal(array):
    maximum = 0
    num_index_errors = 0
    for r in range(0, len(array)):
        for c in range(0, len(array)):
            product = 1
            try:
                # print("R: {0}, C: {1}".format(r, c))
                for s in range(0, 4):
                    # print("\t", array[r + s][c + s])
                    product *= array[r + s][c + s]
            except IndexError:
                num_index_errors += 1
                """
                print("Index error at:"
                      "\n\tRow: {0}"
                      "\n\tColum: {1}"
                      "\n\tShift: {2}"
                      "\n\tTotal IndexErrors: {3}".format(r, c, s, num_index_errors))
                """
                pass
            maximum = find_max(maximum, product)
    return maximum


def find_max_in_dic(dic):
    maximum = 0
    for key in dic:
        maximum = find_max(maximum, dic[key])
    return maximum


def find_max(current_max, challanger):
    if challanger > current_max:
        return challanger
    else:
        return current_max


def print_array(array):
    for row in array:
        print(row)


def print_dic(dic):
    for key in dic:
        print("\t{0}: {1}".format(key, dic[key]))


start_time = time.clock()
main()
print('Time: ', time.clock() - start_time)