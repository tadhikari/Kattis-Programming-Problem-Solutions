'''
https://open.kattis.com/problems/ladder

'''

import math
h,v = map(int,input().split())
l = h/math.sin(math.radians(v))
print(math.ceil(l))

