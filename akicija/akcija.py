'''
https://open.kattis.com/problems/akcija

'''

times = int(input())
prices = []
for i in range(times):
    prices.append(int(input()))
    
prices.sort()
prices

pos = 1
price = 0

while len(prices) > 0:
        if pos%3 == 0:
            prices.pop()
        else:
            price+=prices.pop()
        pos+=1

print(price)
        
        


