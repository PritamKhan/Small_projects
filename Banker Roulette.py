# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# l = len(names)
# x = random.randint(0,l-1)
x = random.choice(names)
print(f"{x} is going to buy the meal today!")
