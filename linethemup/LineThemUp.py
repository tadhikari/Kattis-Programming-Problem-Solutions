times = int(input())
names = []
temp = []
for i in range(times):
    a = input()
    names.append(a)
    temp.append(a)

temp.sort()
if temp[::-1] == names:
    print("DECREASING")
elif temp == names:
    print("INCREASING")
else:
    print("NEITHER")



