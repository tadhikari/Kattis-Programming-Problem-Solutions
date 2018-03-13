'''
https://open.kattis.com/problems/icpcawards
'''

a= int(input())

winner = []
collegeWon = []

for i in range(a):
    team = input().split()
    if team[0] not in collegeWon:
        collegeWon.append(team[0])
        winner.append(team[0]+" "+team[1])

final = ''
for i in range(12):
    if i<11:
        final+=winner[i]+'\n'
    else:
        final+=winner[i]

print(final)
