'''
https://open.kattis.com/problems/humancannonball2
'''

import math

testcases = int(input())
for i in range(testcases):
     v,o,x,h1,h2 = map(float,input().split())
     t = x/(v*math.cos(math.radians(o)))
     y = v*t*math.sin(math.radians(o)) - (0.5*9.81*(t**2))
     if y < h2-1 and y > h1+1:
         print("Safe")
     else:
         print("Not Safe")
