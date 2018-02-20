'''
https://open.kattis.com/problems/faktor

'''
def bribe(a,b):
    b = b-1
    ans = (a*b)+1
    return ans

a,b = map(int,input().split())

print(bribe(a,b))
