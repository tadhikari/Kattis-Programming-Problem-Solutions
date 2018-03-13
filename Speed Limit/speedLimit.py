'''
https://open.kattis.com/problems/speedlimit
'''


while True:
    a = int(input())
    if a == -1:
        break
    else:
        temp = 0
        total = 0
        for i in range(a):
            drive = list(map(int,input().split()))
            total += drive[0] * (drive[1]-temp)
            temp = drive[1]
        print(total,"miles")
