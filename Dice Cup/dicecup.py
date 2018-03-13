'''
https://open.kattis.com/problems/dicecup
'''

a,b = map(int,input().split())

if a==b:
    print(a+1)
else:
    num_of_ans = abs(a-b)+1
    start = min(a,b)+1
    for i in range(start,start+num_of_ans):
        print(i)

