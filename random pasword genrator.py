# passwor genrator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_list=[]
letter = int(input("HOw much letter is need in password : "))
number = int(input("How much number is need in password : "))
symbol = int(input("how much symbol is need in password : "))

for i in range(letter):
    password_list.append(random.choice(letters))

for i in range(number):
    password_list.append(random.choice(numbers))

for i in range(symbol):
    password_list.append(random.choice(symbols))


password_string = ""
for i in password_list:
    password_string += i

print(f"your password will be {password_string} ")

