#Rajnesh Joshi  October 13 2016
print("Welcome To Rajnesh's Crazy Cool Cell Budget Planning")
PAdaytimeandFree=input("Number Of Daytime Minutes?: ")
PAdaytime=PAdaytimeandFree
PAdaytime=float(PAdaytime)
PAdaytime=PAdaytime-100
PAdaytime=PAdaytime*.25
PAevening=input("Number Of Evening Minutes?: ")
PAevening=float(PAevening)
PAevening=PAevening*.15
PAweekend=input("Number Of Weekend Minutes?: ")
PAweekend=float(PAweekend)
PAweekend=PAweekend*.2
if PAdaytime<0:
    PAdaytime=0
    print("You Have No Expenses For Your Daytime Minutes In Plan A Because Your Used Minutes, Does Not Exceed The Free Bonus")
PlanA=PAdaytime+PAevening+PAweekend
print("The Cost Of Plan A is", PlanA,"$")
PBdaytime=PAdaytimeandFree
PBdaytime=float(PBdaytime)
PBdaytime=PBdaytime-250
PBdaytime=PBdaytime*.45
PBevening=float(PAevening)
PBevening=PAevening/.15
PBevening=PBevening*.35
PBweekend=float(PAweekend)
PBweekend=PAweekend/.2
PBweekend=PBweekend*.25
if PBdaytime<0:
    PBdaytime=0
    print("You have No Expenses For Your Daytime Minutes In Plan B Because Your Used Minutes, Does Not Exceed The Free Bonus") 
PlanB=PBdaytime+PBevening+PBweekend
print("The Cost Of Plan B is", PlanB,"$")
if PlanB<PlanA:
    print("Plan B is Cheaper by",PlanA-PlanB,"$")
if PlanB>PlanA:
    print("Plan A is Cheaper by",PlanB-PlanA,"$")
if PlanB == PlanA:
    print("Both Plan A and B are Equal")    
print("Thank You For Using Rajnesh's Crazy Cool Cell Budget Planning")

