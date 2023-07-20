#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print('Welcome to tip calculater')
total_bill = float(input("What is your total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
split = int(input("How many person should split the bill? "))

tip_amount = total_bill * (tip / 100)
bill_payable = total_bill + tip_amount
split_amount = bill_payable / split
# split_amount = round(split_amount, 2)
split_amount = "{:.2f}".format(split_amount)
print(f"Each person should pay: {split_amount}")