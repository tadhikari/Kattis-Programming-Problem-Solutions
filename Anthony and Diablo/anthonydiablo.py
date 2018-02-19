import math

x = input()
a,n = map(float,x.split())

##a circle is the least area covering geometrical shape.

radius = n/(math.pi*2)
area = math.pi * radius**2

if area >= a:
    print('Diablo is happy!')
else:
    print('Need more materials!')
