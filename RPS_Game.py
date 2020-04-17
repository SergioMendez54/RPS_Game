import random

#check answer
# 1 = Rock, 2 = Paper, 3 = Scissors
def check(x, y):
    winner = ""
    if x == 1 and y == 1:
        winner = "It's a tie." 
    if x == 1 and y == 2: 
        winner = "Sorry, PC wins."
    if x == 1 and y == 3:
        winner = "You win!"
    if x == 2 and y == 1:
        winner = "You win!" 
    if x == 2 and y == 2: 
        winner = "It's a tie."
    if x == 2 and y == 3:
        winner = "Sorry, PC wins."
    if x == 3 and y == 1:
        winner = "Sorry, PC wins." 
    if x == 3 and y == 2: 
        winner = "You win!"
    if x == 3 and y == 3:
        winner = "It's a tie"

    return winner
#initiate game

print("___________________________________________")
print("|  This is a Rock, Paper, Scissors Game!  |")
print("|_________________________________________|")
legend = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}

x = 1
while x == 1 or x==2 or x==3:
    y = random.randrange(1,4)
    try: 
        x = int(input("Pick one: \n 1: Rock,  2: Paper,  3: Scissors \n Exit: 0\n"))
        print("PC picked: " + legend.get(y))
        print(check(x,y))

    except ValueError: 
        print("\nNot a valid input, try again: \n")
        continue
 


print("The End. Good game champ.")
