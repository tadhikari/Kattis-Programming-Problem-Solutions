'''

https://open.kattis.com/problems/oddities


'''
run = int(input())
for i in range(run):
    num = int(input())
    if num%2 == 0:
        print('{} is even'.format(num))
    else:
        print('{} is odd'.format(num))
