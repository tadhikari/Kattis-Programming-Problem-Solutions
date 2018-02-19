'''
https://open.kattis.com/problems/simonsays
'''
def simonSays(string):
    string = string.lower()
    if(string[:10] == "simon says"):
        print(string[11:])

times = int(input())
for i in range(times):
   simonSays(input())
