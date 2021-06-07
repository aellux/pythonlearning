from math import *
#print function and variables string
character_name = "John" 
print("There once was a man named John, ")
print("There once was a man named " + character_name + ", ")

#this is a string
print("Giraffe\nAcademy") #\n is new line
print("Giraffe\"Academy") #This prints out quotation mark in the middle

#some functions of python
print(character_name.lower()) # takes the string and converts it to all lowercase, replace lower with upper capitalizes all letters of the string
print(character_name.isupper()) #gives a true or false value depending if the string is capitalized
print(len(character_name)) #prints the number of characters in the string, in this case, 4
print(character_name[0]) #prints the first character/index of the string
print(character_name.index("h")) #prints the position index of the specific character, in this case 2

#working with numbers
print(3+4.5) #adds 3 with 4.5
print(3 * 4 + 5)
print(10%3) #modulus so remainder of divided, 1
my_num = 5
print(my_num)
print(str(my_num) + " my favorite number") #converts the number into a string so you can print # with strings
neg_num = -7
print(abs(neg_num)) #absolute value
print(pow(3, neg_num)) #power 3^-7
print(max(5, 7)) #gets the greater number, 7
print(min(5, 7)) #gets the min number, 5
print(round(3.2)) #rounds the number

#to get more math functions, look at the first line
print(floor(3.7)) #chops off the decimal
print(sqrt(36)) #square root of a number

#getting input from a user
name = input("Please enter a name: ")
age = input("Please enter your age")
print(name)
print(age)

#variable values
#float, int