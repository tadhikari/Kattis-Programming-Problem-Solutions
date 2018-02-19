def average(data):
    total_num_data = int(data[0])
    data = data[2:].split()
    avg = 0
    for i in data:
        avg+= int(i)
    avg = str(avg/total_num_data)
    print(avg)
    decimal  = addDecimal(avg.split('.')[1])
    answer = "{}.{}%".format(avg.split('.')[0],decimal)
    return answer

def addDecimal(decimal):
    if len(decimal) < 3:
        while len(decimal) < 3:
            decimal+='0'
    elif len(decimal) > 3:
        decimal = decimal[:3]

    return decimal

print(average("5 50 50 70 80 100"))
