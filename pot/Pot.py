times = int(input())
total = 0
for i in range(times):
    temp = input()
    number = int(temp[:-1])
    power = int(temp[-1])
    total+= (number**power)
print(total)
    
