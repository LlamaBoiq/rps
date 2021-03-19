import random

wins = int(0)
losses = int(0)

choices = ["rock", "paper", "scissors"]

def lost(): # if u lose
    global losses
    print("you lost. L")
    losses += 1

def won():
    global wins
    print("you won. gg") 
    wins += 1

def draw():
    print("its a draw. lol")


def getnewChoice():
    return random.choice(choices)

def game():
    global losses
    gamerunning = True

    while gamerunning:
        global wins
        global losses
        newchoice = getnewChoice()
        print(f"wins: {wins}\nlosses: {losses}")
        print("1. rock\n2. paper\n3. scissors")
        userinp = input(">> ")
        userchoice = None

        if userinp == '1':
            userchoice = "rock"
        elif userinp == '2':
            userchoice = "paper"
        elif userinp == '3':
            userchoice = 'scissors'
        else:
            print('wot?')
        
        if userchoice == newchoice:
            draw()
        elif userchoice == "rock" and newchoice == "paper":
            print(f"ur choice: {userchoice}\nComputer choice: {newchoice}")
            lost()
        elif userchoice == "rock" and newchoice == "scissors":
            print(f"ur choice: {userchoice}\nComputer choice: {newchoice}")
            won()
        elif userchoice == "scissors" and newchoice == "rock":
            print(f"ur choice: {userchoice}\nComputer choice: {newchoice}") # worst looking code ive ever seen.
            lost()
        elif userchoice == "scissors" and newchoice == "paper":
            print(f"ur choice: {userchoice}\nComputer choice: {newchoice}")
            won()
        elif userchoice == "paper" and newchoice == "scissors":
            print(f"ur choice: {userchoice}\nComputer choice: {newchoice}")
            lost()
        elif userchoice == "paper" and newchoice == "rock":
            print(f"ur choice: {userchoice}\nComputer choice: {newchoice}")
            won()

game() # plays game
