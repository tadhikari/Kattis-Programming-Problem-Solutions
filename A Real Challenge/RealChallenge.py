import math

def fenceLength(length):
    return 4*length


def getLength(area):
    side = math.sqrt(area)
    return side


print(fenceLength(getLength(int(input()))))
