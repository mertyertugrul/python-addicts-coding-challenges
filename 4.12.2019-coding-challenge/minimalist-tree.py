#!/bin/python3

import math
import os
import random
import re
import sys


class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return '(' + str(self.left) + ':L ' + "V:" + str(self.value) + " R:" + str(self.right) + ')'


def minimalist_tree(arr, start=None, end=None):
    if start is None and end is None:
        start = arr[0]
        end = arr[len(arr) - 1]
    if start > end:
        return None

    median = (end + start) // 2

    root = Node(median)
    root.left = minimalist_tree(arr, start, median - 1)
    root.right = minimalist_tree(arr, median + 1, end)
    return root


if __name__ == '__main__':
    try:
        arr = list(map(int, input().split(',')))
    except:
        arr = list()

    output = minimalist_tree(arr)
    if output is None:
        print('None')
    else:
        print(output)
