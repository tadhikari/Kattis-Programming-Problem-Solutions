'''
https://open.kattis.com/problems/judgingmoose

'''

l,r = map(int,input().split())

if l==r and l!=0 and r!=0:
    print('Even {}'.format(2*l))
elif l == 0 == r:
    print('Not a moose')
else:
    print('Odd {}'.format(2*max(l,r)))
