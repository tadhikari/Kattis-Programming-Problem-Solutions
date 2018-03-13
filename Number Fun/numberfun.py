'''
https://open.kattis.com/problems/numberfun
'''

a = int(input())

for i in range(a):
    a,b,c = map(int,input().split())
    if a+b == c or a/b == c or b/a == c or a-b==c or b-a==c or a*b==c:
        print('Possible')
    else:
        print('Impossible')
