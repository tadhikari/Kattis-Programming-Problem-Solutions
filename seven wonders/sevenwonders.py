'''
https://open.kattis.com/problems/sevenwonders
'''

a = input()

t = a.count('T')
c = a.count('C')
g = a.count('G')

extra = 0
if t>0 and c>0 and g>0:
    extra = 7*min([t,c,g])

total = t**2+c**2+g**2+extra
print(total)
