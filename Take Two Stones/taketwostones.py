def whoWins(number_of_stones):
    if number_of_stones%2==0:
        return "Bob"
    else:
        return "Alice"


print(whoWins(int(input())))
