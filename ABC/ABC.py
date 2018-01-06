##num = input()
##num = num.split()
##for i in range(len(num)):
##    num[i] = int(num[i])
##num.sort()
##
##temp = ["A":num[0], "B":num[1], "C":num[2]]

num = input()

order = input()

def orderNum(num,order):
    answer = []
    num = num.split()
    for i in range(len(num)):
        num[i] = int(num[i])
    num.sort()
    temp = {"A":num[0], "B":num[1], "C":num[2]}
    for i in order:
        answer.append(str(temp.get(i)))

    return answer[0]+" "+answer[1]+" "+answer[2]


print(orderNum(num,order))
