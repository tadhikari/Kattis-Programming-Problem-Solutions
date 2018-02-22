
'''
https://open.kattis.com/problems/sibice
'''

import math
nwh = list(map(int,input().split()))
diagnol = math.sqrt(nwh[1]**2+nwh[2]**2)

for i in range(nwh[0]):
    length = int(input())
    if length <= diagnol:
        print('DA')
    else:
        print('NE')

#tip: compare the length with diagnol of the box. (diagnol is the largest possible length in a rectangle)

