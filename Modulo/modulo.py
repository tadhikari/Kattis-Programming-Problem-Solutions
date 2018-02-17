'''

https://open.kattis.com/problems/modulo


'''

num = []
for i in range(10):
    num.append(int(input()))
modulo = [i%42 for i in num]
print(len(set(modulo)))
