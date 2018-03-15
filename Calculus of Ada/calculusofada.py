'''https://open.kattis.com/problems/ada'''

def differences(num):
    a = []
    for i in range(1,len(num)):
        a.append(num[i]-num[i-1])
    return a

def reachedFinalStage(differences):
    return all(i==differences[0] for i in differences)

def order_and_next(outputs):
    a = []
    a.append(outputs)
    counter = 0
    
    while not reachedFinalStage(outputs):
        outputs = differences(outputs)
        a.append(outputs)
        counter+=1
        
    last = 0
    for i in a:
        last+=i.pop()

    print(counter,last)


a = list(map(int,input().split()))
order_and_next(a[1:])
