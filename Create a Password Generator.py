
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_number = int(input("How many number would you like?\n"))
nr_symbol = int(input("How many symbols would you like?\n"))

#level 1
# password = ""

# for i in range(0, nr_letters):
#     password += random.choice(letters)
    
# for i in range(0, nr_number):
#     password  += random.choice(numbers)
    
# for i in range(0, nr_symbol):
#     password += random.choice(symbols)
    
# print(password)   

#level 2
password = []
for i in range(0, nr_letters):
    password += random.choice(letters)
    
for i in range(0, nr_number):
    password  += random.choice(numbers)
    
for i in range(0, nr_symbol):
    password += random.choice(symbols)
    
random.shuffle(password)
print ("Your password is: ",''.join(password))
