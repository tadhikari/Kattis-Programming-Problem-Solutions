'''
https://open.kattis.com/problems/symmetricorder
'''

setno = 1
while True:
    a = int(input())
    if a == 0:
        break
    else:
        current_set = []
        for i in range(a):
            name = input()
            current_set.append(name)
        ans_set = current_set[::2]+current_set[1::2][::-1]
        print("SET {}".format(setno))
        for j in ans_set:
            print(j)
        setno+=1

            
