'''
https://open.kattis.com/problems/quadrant
'''

x = int(input())
y = int(input())

if x>0 and y>0:
    answer = 1
elif x<0 and y>0:
    answer = 2
elif x<0 and y<0:
    answer = 3
elif x>0 and y<0:
    answer = 4


print(answer)
