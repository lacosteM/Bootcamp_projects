import math

print("Welcome to the finance calculator")
#ask the user wheather they would like investment or bond
user_choice = input("Would you like to go to 'investment' or 'bond': ")

if user_choice == "investment":

    depost_amount = float(input("How much money are you depositing: "))
    interest_rate = float(input("How much interest would you like on your deposit(as a percentage): "))
    years = int(input("number of years they plan to invest: "))
    interest = input(" Would you like 'Simple' or 'Compound' interest: ").lower()
  
    #Conevert the interest rate into a decimal 
    t = interest_rate / 100
    
    #calulate the total amount based on interest type 
    if interest == "Simple": 
    #This is the simple interest formula
        total = depost_amount*(1 + t*years)
    #This is the compound interest formula
    elif interest == "Compound":
        total =  depost_amount * math.pow((1+t),years)
    else:
        print("please enter a valid interest choice. Enter either 'simple or 'compound'.")
    

 #prints the results based on user choice 
    print("Your investment will be worth",round(total, 2))

elif user_choice == "bond":

    house_value  = int(input("How much is the value of your current house: "))
    bond_interest_rate = int(input("Enter the interest rate on your house: "))
    months = int(input("How many months do you plan on repaying the bond: "))

    #The bond repayment calulations
    monthly_interest_rate = bond_interest_rate / 100 / 12
    repayment = (monthly_interest_rate * house_value) /(1 - math.pow(1 + monthly_interest_rate, -months))

    print("Your monthly bond repayment will be:", round(repayment, 2))
    
    
else: print("Please select between bond or investment")






