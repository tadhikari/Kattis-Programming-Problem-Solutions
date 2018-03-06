def factors(n):
    factors = 0
    factor = 2
    while factor**2 <= n:
        if n%factor == 0:
            n/=factor
            factors+=1
        else:
            factor+=1
    return factors+1

n = int(input())
print(factors(n))
