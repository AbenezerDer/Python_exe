# use for loop through the list from 1 to 21
for  i in range(1, 21):

# use modulus to check that the result is not equal to 0
    if ((i % 2) != 0):

# print the odds
    print("i = ", i)
    
# Have the user enter their investment amount and expected interest
# Each year their investment will increase by their investment + their investment * interest rate is 
# print out the earnigns after a 10 year period 

# Ask for the money invested + the interest rate 
money = input("How much to invest : ")
interest_rate = input("Interest rate : ")
# convert the value to a float
money = float(money)

# convert value to a float and round the percentage rate by 2 digits
interest_rate = float(interest_rate)* .01

# cycle through 10 year using a for loop and range from 0 to 9
for i in range(10):
    money = money + (money * interest_rate)
# output the results
print("Investment after 10 years : {:.2f}".format(money))
    