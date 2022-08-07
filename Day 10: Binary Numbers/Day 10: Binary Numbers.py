#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    k= str(bin(n))
    c=1
    p=[]
    for i in range(2,len(k)-1):
        if  k[i]=="1" and k[i+1]=="1":
            c = c+1
            p.append(c)
        else:
            c = 1
            p.append(c)
    print(max(p))
