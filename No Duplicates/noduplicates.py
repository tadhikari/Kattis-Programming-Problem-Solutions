'''
https://open.kattis.com/problems/nodup
'''

def isRepeat(a):
    for i in a:
        if a.count(i)>1:
            return "no"
    return "yes"


a = input().split()
print(isRepeat(a))













