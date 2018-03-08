
'''
https://open.kattis.com/problems/planina

'''
initial_side = 2 #at initial state a side ocntains 2 points

iteration = int(input())

num_of_points = initial_side

for i in range(iteration):
    points = (initial_side + (initial_side - 1))
    num_of_points = points**2
    initial_side = points

print(num_of_points)

