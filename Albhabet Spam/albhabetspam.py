#Asci 65-90 capital letters
#Asci 97-122 small letters
#Asci 32 is space
#other charecters
'''
https://open.kattis.com/problems/alphabetspam
'''
num_capital = 0
num_small = 0
num_char = 0
num_space = 0


string = input()

len_string = len(string)


for i in string:
    if ord(i) >=65 and ord(i) <= 90:
        num_capital+=1
    elif ord(i) >= 97 and ord(i) <= 122:
        num_small+=1
    elif i == "_":
        num_space+=1
    else:
        num_char+=1


print(str(num_space/len_string)+"\n"+str(num_small/len_string)+"\n"+str(num_capital/len_string)+"\n"+str(num_char/len_string))

