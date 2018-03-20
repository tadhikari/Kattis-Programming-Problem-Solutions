'''
https://open.kattis.com/problems/deathknight
'''

n = int(input())
total = 0
for i in range(n):
    a = input()
    if "CD" not in a:
        total+=1

print(total)
