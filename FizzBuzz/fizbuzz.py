'''
https://open.kattis.com/problems/fizzbuzz
'''

num = list(map(int,input().split()))
for i in range(1,num[2]+1):
    if i%num[0]==0 and i%num[1] == 0:
        key = 'FizzBuzz'
    elif i%num[1]==0:
        key = 'Buzz'
    elif i%num[0] == 0:
        key = 'Fizz'
    else:
        key = i
    print(key)

