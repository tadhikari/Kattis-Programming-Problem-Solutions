'''
https://open.kattis.com/problems/stararrangements
'''

def addup(a,b,c):
    total = 0
    while total < c:
        total+=b
        if total!=c:
            total+=a
    return total==c

a = int(input())
print(str(a)+":")
for i in range(2,((a//2)+2)):#you dont need to check till the number only till half
    if addup(i-1,i,a):
        print(i,i-1,sep=",")
    if addup(i,i,a):
        print(i,i,sep=",")
