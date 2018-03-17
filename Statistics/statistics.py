'''
https://open.kattis.com/problems/statistics
'''

import sys

case = 1

for line in sys.stdin.readlines():
    a = list(map(int,line.split()[1:]))
    minimum = min(a)
    maximum = max(a)
    diff = maximum - minimum
    print("Case {}: {} {} {}".format(case,minimum,maximum,diff))
    case+=1
