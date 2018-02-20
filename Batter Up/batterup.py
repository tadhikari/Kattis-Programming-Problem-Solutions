'''
https://open.kattis.com/problems/batterup
'''
bat = int(input())
plays = input().split()
total = 0
for i in plays:
    if int(i) < 0:
        bat+=int(i)
    else:
        total+= int(i)
print(total/bat)
