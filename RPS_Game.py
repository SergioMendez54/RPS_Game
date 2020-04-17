import random

#check answer
# 1 = Rock, 2 = Paper, 3 = Scissors
def check(x, y):
    winner = ""
    if x == y:
        return "It's a tie.\n"
    if x == 1 and y == 2: 
        winner = "b"
    if x == 1 and y == 3:
        winner = "a"
    if x == 2 and y == 1:
        winner = "a" 
    if x == 2 and y == 3:
        winner = "b"
    if x == 3 and y == 1:
        winner = "b" 
    if x == 3 and y == 2: 
        winner = "a"

    if winner == "a":
        return "Player 1 wins with {} beating {}!\n".format(legend.get(x), legend.get(y))
    if winner == "b":
        return "Computer wins with {} beating your {}.\n".format(legend.get(y), legend.get(x))
#initiate game

print("___________________________________________")
print("|  This is a Rock, Paper, Scissors Game!  |")
print("|_________________________________________|")
legend = {
    1: "Rock",
    2: "Paper",
    3: "Scissors",
    "a": "Player 1",
    "b": "Computer"
}

x = 1
while x==1 or x==2 or x==3:
    y = random.randrange(1,4)
    try: 
        x = int(input("Choices: 1-Rock,  2-Paper,  3-Scissors  : "))
        print("You selected: {}".format(legend.get(x)))
        print("PC randomly picked: {}".format(legend.get(y)))
        print(check(x,y))

    except ValueError: 
        print("\nNot a valid input, try again: \n")
        continue
    playagain = input("Play again? Enter \"y\" or \"n\": ")
    if playagain != "y":
        break


print("The End. Good game champ.\n")
input("Press any key to exit. ")
