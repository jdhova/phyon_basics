#### check if coffee is on then ask what coffee you want
#### whrn you choose then calculate how much incridiates needed
####
####
####
###

is_On = True
choice = []

## balance
milk = 100
sugar = 50
water = 500

Ingridients = {milk:100,sugar:50,water:50}

Capuchino = {milk:10,sugar:5,water:15}

### check balance of coffee



def coffee():
 choice = []
 while is_On:
    choice = input("What will you like to have? Expresso/Late/Capuchino : ")
    choice = [x for x in choice if(len(choice) > 0)]
    choice2 = ("".join(choice))
    ##print(choice2,"im here")
    if choice2 == "Capuchino":
      while Ingridients:
       if((Ingridients["milk"] > Capuchino["milk"]) and (Ingridients["sugar"] > Capuchino["sugar"]) and (Ingridients["water"] > Capuchino["water"])):
        print("Capchio ready")

 coffee()  
   




# while is_On:
#     if (is_On =="False"):
#         print("coffee Off")
#         break
    
#     else: choice = input("What will you like to have? Expresso/Late/Capuchino : ")
#     choice = [x for x in choice if(len(choice) > 0)]
#     print(choice,"im here")
        




