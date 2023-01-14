#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 11:19:08 2021

@author: erik
"""
import numpy as np
from matchLines_Total import matchLines_total

test_array1 = np.transpose([[1, 2, 3, 4, 5], [55, 77, 88, 10, 99]]) #model

test_array2 = np.transpose([[1, 2, 9, 4, 5], [22, 66, 33, 44, 11]]) #data

# print('test array 1 =\n', test_array1)
# print('test array 2 =\n', test_array2)

a = matchLines_total(test_array1, test_array2, 2)
print('a2 =', a)

# a = np.delete(a, np.where(a == 0), axis = 0)


# print('second a =', a)
