'''
https://open.kattis.com/problems/grassseed
'''


price = float(input())
num = int(input())

total_area = 0
for i in range(num):
    w,l = map(float,input().split())
    total_area+=(w*l)

print(total_area*price)
