'''
https://open.kattis.com/problems/conundrum
'''

cipher = "PER"
initial_text = input()
index = 0
days = 0
for i in initial_text:

    if index>2:
        index = 0

    if i!=cipher[index]:
        days+=1

    index+=1

print(days)
    
