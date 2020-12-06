#Rajnesh Joshi November 2nd 2016
from random import randint
wallet=1000
num=int(randint(1,38))
randcolor=int(randint(1,2))
if randcolor==1:
    colour=1
if randcolor==2:
    colour=2
run=1
while run:
    print("Hello and Welcome To Rajnesh's Roulette Game")
    print("The Rules Are Simple:")
    print("You Have To Choose Between Red and Black.")
    print("If The Ball Lands On Your Colour, I'll give you twice your bet")
    print("If The Ball Also Lands On Your Number, I'll give you 10x your bet")
    print("However if your'e guess is between a +3 or -3 range I'll give you a win")
    print("Got It? Let's Go!")
    bet=int(input("How Much Money Do You Bet?: "))
    colourchoice=input("What Colour Do You Think The Ball Will Land On: ")
    if colourchoice == "Red":
        if colour == 2:
            bet=bet*2
    if colourchoice == "Black":
        if colour == 1:
            bet=bet*2
    if colourchoice == "Red":
        if colour== 1:
            wallet=wallet-bet
    if colourchoice == "Black":
        if colour == 2:
            wallet=wallet-bet
    numberchoice=input("What Number Do You Think The Ball Will Land On: ")
    if numberchoice == num:
        bet=bet*10
    if numberchoice == num-1:
        bet=bet*10
    if numberchoice == num-2:
        bet=bet*10
    if numberchoice == num-3:
        bet=bet*10
    if numberchoice == num+1:
        bet=bet*10
    if numberchoice == num+2:
        bet=bet*10
    if numberchoice == num+3:
        bet=bet*10
    elif numberchoice:
        wallet=wallet-bet
    print("You Now Have",wallet+bet)
    if numberchoice == num:
        print("You Have Guess The Correct Number So I Give You Youre Money")
    elif numberchoice:
        print("You Have Guessed The Wrong Number i will Take You Bet Now")
    if colourchoice == "Red":
        if colour == 2:
            print("You Have Guessed The Right Colour I Will Give You Your Money")
    if colourchoice == "Black":
        if colour == 1:
            print("You Have Guessed The Right Colour I Will Give You Your Money")
