'''
https://open.kattis.com/problems/easiest
'''
a = int(input())

while a > 0:
    i = 11
    n_sum = sum(map(int,list(str(a))))
    while True:
        product = list(str(a * i))
        chars = sum(map(int,product))
        if chars == n_sum:
            print(i)
            break
        i+=1
        
    a = int(input())

        
    
