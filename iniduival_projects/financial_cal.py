#IC 1st financial calucolator

#define the saving function 
def saving_function():
    #asking how muchy they want to save
    goal = float(input("How much do you want to save? "))
    # asking the user how often they are adding onto the account 
    option = input("how often do you want to add to it 1 = weekly and 2 is = monthly ")
# two options 
    
# 1 = weekly 
# 2 = monthly 
    if option == "1":
        # how much are they going to add
        amount = float(input("how much will you save each week?")) 
        #caluclate weeks 
        weeks = goal / amount  
        #show to user      
        print(f" it will take you{weeks} weeks to get your goal ")       
    elif option == "2":
        #asking how much amount wise
        amount = float(input("how much will you save each month"))
        #calucating for months
        months = goal / amount
        #SHOW THE USER THE INFO 
        print(f"it will take you aboiut {months} months to reach your goal")
    else:
        print("incorrect vaule")


# define function budget allocatior 
def budget_allocator():
#asing how much monthly income
    income = float(input("how much do you get per month"))
# asking how much catorgies they have
    catgories = int(input("how muich budget categoires do you have? "))
    #setting loop so it doesnt stop 
    for i in range(catgories):
        #asking the name of it
        name = input("Enter category name:")
        #ask user how much tehy want go in each 
        percent = float(input(f"what is percentage for{name}"))
        #caucalte 
        amount = income * (percent / 100)
# calucaltor percentage for each one and then print
        print(f"{name} would have $ {percent} of your money")                    

# define sales cal
def sales_cal(): 
# asking og price
    og_price = float(input("what was the orgianl price?"))
# ask for discount
    discount = float(input("what is the discount"))
# calucate discount 
    final = og_price - (og_price * discount / 100)
#og price - discount = new price
# print new price
    print(f"the price after discount is {final}")


# define tip calucasltor 
def tip_calculator():
    # asking price of meal 
    meal_price = float(input("Enter meal price: "))
    # amount of tip they want to give 
    tip_percent = float(input("Enter tip percentage: "))
    # caulcator tip 
    tip = meal_price * (tip_percent / 100)
    total = meal_price + tip
# caulcate tip 
    print("Tip amount:", tip)
    print("Total bill:", total)
# i forgot about compund instrest thingy i didn't know what that was so internat to save
#thanks google 
# no worries i asked it to explain it 
def compound_interest_calculator():
    # so this is us askking for starting amount
    principal = float(input("Enter the starting amount: "))
    #rates and then turning them into percenatage 
    rate = float(input("Enter annual interest rate (%): ")) / 100
    #how many times is it mutplied so like 12
    times = int(input("How many times per year is interest compounded? "))
    # hoiw many years you dont wanna touch your money
    years = float(input("How many years will you invest? "))
    # the equation for it 
    amount = principal * (1 + rate / times) ** (times * years)
    #showing user the final thing
    print("Final amount:", amount)                          


def menu():

#ask the user what options they want display options 
    print("choose an option:")
    print("1 = savings cal ")
    print("2 = budget allocater")
    print("3 = tip calculator")
    print("4 = sales cal")
    print("5 = compound interest cal")
    #they get a choice 
    choice = input("enter your choice: ")
# play the function for that chocie
    #this is the same thing I bulit for my game :)
    if choice == "1":
        saving_function()
    elif choice == "2":
        budget_allocator()
    elif choice == "3":
        tip_calculator()
    elif choice == "4":
        sales_cal()
    elif choice == "5":
        compound_interest_calculator()
    else:
        print("invaild choice")
menu()
