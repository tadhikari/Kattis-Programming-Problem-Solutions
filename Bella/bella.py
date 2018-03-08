'''
https://open.kattis.com/problems/bela
'''

dic = {'A':[11,11], 'K':[4,4], 'Q':[3,3], 'J':[20,2],
       'T':[10,10], '9':[14,0], '8':[0,0], '7':[0,0]}

total = 0
multiplier, trump = input().split()
for i in range(4*int(multiplier)):
    card = input()
    if card[1] == trump:
        total+=dic.get(card[0])[0]
    else:
        total+=dic.get(card[0])[1]
        
print(total)
