'''

https://open.kattis.com/problems/nastyhacks


'''
times = int(input())
for i in range(times):
    line = list(map(int,input().split()))
    diff = line[1]-line[2]
    rev = line[0]
    if diff > rev:
        output = "advertise"
    elif diff == rev:
        output = "does not matter"
    elif diff < rev:
        output = "do not advertise"
    print(output)
