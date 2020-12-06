#Rajnesh Joshi November 1st 2016
import random
wallet = 100
run = 1
while run == 1:
    print("Lucky 7 Betting Game. You Will Bet")
    dice1=random.randint(1, 6)
    dice2=random.randint(1, 6)
    dice_total = dice1 + dice2
    bet = int(input("Enter How Much You'd Like  To  Bet: "))
    print("1 For Less  Than 7")
    print("2 For Equal To 7")
    print("3 For Greater Than 7")
    pick= int(input("What Do You Choose?: "))
    if (pick == 1) and (dice_total < 7):
        print("Dice Rolls",dice_total,"You Win!")
        wallet = wallet+bet
    elif (pick == 2) and (dice_total==7):
        print("Dice Rolls", dice_total, "You Win!")
        wallet=wallet + (2 * bet)
    elif (pick==3) and (dice_total >7):
        print("Dice Rolled", dice_total,"You Win!")
    else:
        print("Dice rolles", dice_total,"You  Lose")
        wallet = wallet - bet
    print("You Now Have", wallet,"dollars")
