'''https://open.kattis.com/problems/4thought'''

def fours(n):

    if n>256 or n<-256:
        return None

    

    usage = ['+', '-','//','*']

    for i in usage:
        for j in usage:
            for k in usage:
                combination = '4 '+i+' 4 '+j+' 4 '+k+' 4'
                #print(i,j,k,' ==> ',combination,' ==> ',eval(combination))
                if eval(combination) == n:
                    if '//' in combination:
                        combination = combination.replace('//','/')

                    return combination + ' = {}'.format(n)
    


times = int(input())

for i in range(times):
    result = fours(int(input()))
    if result == None:
        print('no solution')

    else:
        print(result)
