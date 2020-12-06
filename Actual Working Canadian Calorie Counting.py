#Rajnesh Joshi October 10 2016
def Calorie_Counter():
    print("Welcome to Rajnesh's Canadian Calorie Counting Majiggy Machine")
    print("Press 1 For Cheeseburger")
    print("Press 2 For Fish Burger")
    print("Press 3 For Veggie Burger")
    print("Press 4 For No Burger")
    burger=input("Please Enter Burger Choice: ")
    if burger == "1":
        burger=float(461)
    if burger == "2":
        burger=float(431)
    if burger == "3":
        burger=float(420)
    if burger == "4":
        burger=float(0)
    print("Press 1 For Soft Drink")
    print("Press 2 For Orange Juice")
    print("Press 3 For Milk")
    print("Press 4 For No Drink")
    drink=input("Please Enter Drink: ")
    if drink == "1":
        drink=float(130)
    if drink == "2":
        drink=float(160)
    if drink == "3":
        drink=float(118)
    if drink == "4":
        drink=float(0)
    print("Press 1 For Fries")
    print("Press 2 For Baked Potato")
    print("Press 3 Chef Salad")
    print("print 4 No Side Order")
    sideorder=input("Please Enter Side Choice: ")
    if sideorder == "1":
        sideorder=float(100)
    if sideorder == "2":
        sideorder=float(57)
    if sideorder == "3":
        sideorder=float(70)
    if sideorder == "4":
        sideorder=float(0)
    print("Press 1 For Apple Pie")
    print("Press 2 For Sundae")
    print("Press 3 For Fruit Cup")
    print("Press 4 For No Dessert")
    dessert=input("Please Enter Dessert: ")
    if dessert=="1":
        dessert=float(167)
    if dessert=="2":
        dessert=float(266)
    if dessert=="3":
        dessert=float(75)
    if dessert=="4":
        dessert=float(0)
    print("Your Total Calorie Count Is")
    print(burger+drink+sideorder+dessert)
    again=input("Would you like to use this again: ")
    if again == "yes":
        Calorie_Counter()
    if again == "no":
        quit()
Calorie_Counter()
again=input("Would you like to use this again: ")
