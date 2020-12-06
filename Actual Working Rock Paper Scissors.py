#Rajnesh Joshi October 31 2016
from random import randint
x=int(randint(1,30))
y=int(randint(1,30))
run=1
while run:
    print("Hello, and Welcome To Rajnesh's Rock Paper Scissor Game")
    print("You Can Choose One Of The Following")
    print("Rock")
    print("Paper")
    print("Scissors")
    handsign=input("What Do You Choose?: ")
    if handsign == "Rock":
        if x>y:
            print("Computer Chose Scissors, You Win")
        if x<y:
            print("Computer Chose Paper, You Lose")
        if x==y:
            print("Computer Chose Rock, Tie")
    if handsign == "Paper":
        if x>y:
            print("Computer Chose Rock, You Win")
        if x<y:
            print("Computer Chose Scissors, You Lose")
        if x==y:
            print("Computer Chose Paper, Tie")
    if handsign == "Scissors":
        if x>y:
            print("Computer Chose Paper, You Win")
        if x<y:
            print("Computer Chose Rock, You Lose")
        if x==y:
            print("Computer Chose Scissors, Tie")
    if handsign == "Scissor":
        if x>y:
            print("Computer Chose Paper, You Win")
        if x<y:
            print("Computer Chose Rock, You Lose")
        if x==y:
            print("Computer Chose Scissors, Tie")

    playerscore=int(0)
    computerscore=int(0)
    if x>y:
        playerscore=playerscore+1
    if x<y:
        computerscore=computerscore+1
    print("Player's Score",playerscore)
    print("Computer's Score",computerscore)
