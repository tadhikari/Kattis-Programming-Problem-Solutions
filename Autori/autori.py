def shortForm(word):
    if "-" in word:
        words = word.split("-")
    else:
        words = [word]
    shortTerm = ''
    for i in words:
        shortTerm += i[0]

    return shortTerm

print(shortForm(input()))
    
