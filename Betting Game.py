from random import randint
x=int(randint(1,7))
player=float(100)
print("Pick 1 Of These")
print("1 if you think the number will be more than 7")
print("2 if you think the number will be equal to 7")
print("3 if you think the number will be less than 7")
money=input("How Much Do You Bet: ")
choice=input("What do you choose: ")
if choice == "1":
    if x>7:
        print("You Are Right")
    if x<7:
        print("You Are Wrong")
    if x==y:
        print("You Are Wrong")
if choice == "2":
    if x>7:
        print("You Are Wrong")
    if x<7:
         print("You Are Wrong")
    if x==y:
        print("You Are Right")
if choice == "3":
    if x>7:
        print("You Are Wrong")
    if x<7:
         print("You Are Right")
    if x==y:
        print("You Are Wrong")
