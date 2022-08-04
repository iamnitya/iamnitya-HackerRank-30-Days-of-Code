#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().split()))
    k = (arr[::-1])
    for i in k:
        print(i, end =" ")
