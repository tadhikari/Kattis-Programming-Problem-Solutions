dictionary = {'a':'@','b':'8','c':'(','d':'|)','e':'3','f':'#','g':'6',
              'h':'[-]','i':'|','j':'_|','k':'|<','l':'1','m':'[]\/[]',
              'n':'[]\[]','o':'0','p':'|D','q':'(,)','r':'|Z','s':'$','t':"']['",
              'u':'|_|','v':'\/','w':'\/\/','x':'}{','y':'`/','z':'2'}

def newAlphabet(string):
    string = string.lower()
    new = ''
    for i in string:
        if dictionary.get(i) == None:
            new+=i
        else:
            new+=dictionary.get(i)
    return new

print(newAlphabet(input()))
