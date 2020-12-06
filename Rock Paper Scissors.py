#Rajnesh Joshi October 27 2016
from random import randint
x=int(randint(1,30))
y=int(randint(31,60))
z=int(randint(61,100))
rock=int(x)
scissor=int(y)
paper=int(z)
print("Hello, and Welcome To Rajnesh's Rock Paper Scissor Game")
print("You Can Choose One Of The Following")
print("Rock")
print("Paper")
print("Scissors")
ask=input("What Do You Choose")
if ask == "Rock":
    print("Please A Number 1-30 For Rock")
    handsign=input(float("Please Choose: "))
    if handsign == handsign>x:
        print("Computer Chose Scissors, You Win")
    if handsign == handsign<x:
         print("Computer Chose Paper, You Lose")
if ask == "Paper":
    print("Please Enter A Number 31-60 For Paper")
    handsigny=float(input("Please Choose: "))
    if handsigny == handsigny>y:
        print("Computer Chose Rock, You Win")
    if handsigny == handsigny<y:
        print("Computer Chose Scissors, You Lose")
if ask == "Scissors":
    print("Please Enter A Number 61-100 For Scissors")
    handsignz=input(float("What Do You Choose: "))
    if handsignz == handsign>z:
        print("Computer Chose Paper, You Win")
    if handsignz == handsign<z:
        print("Computer Chose Rock, You Lose")
