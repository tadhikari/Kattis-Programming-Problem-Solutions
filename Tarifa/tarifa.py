
'''
https://open.kattis.com/problems/tarifa
'''

rate = int(input())
months = int(input())
total = 0
for i in range(months):
    total+=(rate-int(input()))
print(total+rate)
