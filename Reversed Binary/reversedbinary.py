'''
https://open.kattis.com/problems/reversebinary
'''

def d2b(num):
    rem = ''
    while num > 0:
        rem += str(num%2)
        num = num//2
        
    return rem[::-1] 

def b2d(num):
    total = 0
    for i in range(len(num)):
        total+=(int(num[i]) * 2**i)
    return total

print(b2d(d2b(int(input()))))
