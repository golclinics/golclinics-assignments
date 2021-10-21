import collections
import math
import os
import random

def rotate_left(A, d):
    #deque to make it a stand queue not array
    rot_a=collections.deque(A)
    #rotate list. - for left shift + for right shit
    rot_a.rotate(-d)
    #turn back to  list from queue
    A=list(rot_a)
    return A


A = [3, 2, 1, 10, 15, 3] 
d = 3
print (rotate_left(A, d))