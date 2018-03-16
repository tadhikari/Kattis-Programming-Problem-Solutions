'''
https://open.kattis.com/problems/zamka
'''

start = int(input())
end = int(input())
total = int(input())

possible_answers = []

for i in range(start,end+1):
    a = sum(map(int,list(str(i)))) #breaking num into char and summing it all up
    if a==total:
        possible_answers.append(i)

print("{}\n{}".format(min(possible_answers),max(possible_answers))) # min of our range and max of our range
