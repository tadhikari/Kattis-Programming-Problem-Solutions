'''
https://open.kattis.com/problems/cetvrta
'''
def getPoint(known_x,Known_y):
    final_x = odd_one_out(known_x)
    final_y = odd_one_out(known_y) #bsaed on the fact that a rectangle will always have 2 points which have same x or y cordinates
    return final_x,final_y

def odd_one_out(a):
    occurance = [a.count(a[0]), a.count(a[1]), a.count(a[2])]
    odd = min(occurance)
    odd_one = occurance.index(odd)
    return (a[odd_one])

known_x = []
known_y = []

for i in range(3):
    x,y = input().split()
    known_x.append(x)
    known_y.append(y)

ans = getPoint(known_x,known_y)

print(ans[0],ans[1])
