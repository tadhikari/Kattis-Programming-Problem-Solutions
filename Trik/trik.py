
'''
https://open.kattis.com/problems/trik
'''

def moveA(cups):
    temp = cups[1]
    cups[1] = cups[0]
    cups[0] = temp
    return cups


def moveB(cups):
    temp = cups[2]
    cups[2] = cups[1]
    cups[1] = temp
    return cups

def moveC(cups):
    temp = cups[0]
    cups[0] = cups[2]
    cups[2] = temp
    return cups
    

cups = ['A','B','C']

order = input()

for i in order:
    if i == 'A':
        cups = moveA(cups)
    elif i == 'B':
        cups = moveB(cups)
    elif i == 'C':
        cups = moveC(cups)

print(cups.index('A')+1)
