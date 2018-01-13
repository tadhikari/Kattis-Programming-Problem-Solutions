def name(name):
    temp = ''
    answer = ''
    for i in name:
        if temp!= i:
            answer+=i

        temp = i
    return answer

print(name(input()))
