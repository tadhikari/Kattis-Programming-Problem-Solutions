'''
https://open.kattis.com/problems/addingwords
'''
from sys import stdin

data = {}

def assign(line,data):
    data[line[1]] = line[2]

def calc(line,data):
    temp = ''
    for i in line:
        if i!='+' and i!='-' and i!='=':
            if data.get(i)!=None:
                temp+=data.get(i)
            else:
                return "unknown"
        else:
            temp+=i
    inv_mapping = {v:k for k,v in data.items()}
    final = inv_mapping.get(str(eval(temp[:-1])))
    if final == None:
        return "unknown"
    else:
        return final

for line in stdin.readlines():
    words = line.split()
    if words[0] == 'def':
        assign(words,data)
    elif words[0] == 'calc':
        print("{} = {}".format(line[5:-2],calc(words[1:],data)))
    elif words[0] == 'clear':
        data = {}
        


    
