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

#creating/using a list
friends = ["Kevin", "Karen", "Jim", "Jin", "Alex"]
print(friends[2]) #prints the index of "Jim" which is in the 2nd index
print(friends[-1]) #prints the index starting from the end, which is Alex
print(friends[1:3]) #prints the index from 1 onward until the 3rd, can leave 3 empty to print all indexes from 1 onward

friends[1] = "Mike" #Edits the element in the list
print(friends[1]) 

#list functions
lucky_numbers = [4,8,4,6,7,8,10]
friends.extend(lucky_numbers) #adds the list of lucky numbers onto the friends list
friends.append("Potato") #adds another name at the end of the list
friends.insert(1, "Kelly") #at index position 1, it adds Kelly into the list, moving the rest of the list to +1 index
friends.remove("Jim") #removes a specific element in the list
friends.clear() #function to remove the entire list
friends.pop() #removes the last element in the list
print(friends.index("Kevin")) #prints the index of the specific element of the list
print(friends.count("Jim")) #prints the number of "Jim" elements in the list
friends.sort() #puts the elements in alphabetical order, in terms of numbers, goes least to greatest
lucky_numbers.reverse() #reverses the order of the list
friends2 = friends.copy() #friends2 copies the same elements in friends

#tuples
coordinates = (5, 6) #permanent elements in the tuple, cannot be changed
print(coordinates[0]) #prints the first index of the coordinates list
coordinatesL = [(4, 5), (6, 7), (8, 9)] #you can make a list of tuples

#functions
def say_hi(name, age):
    print("Hi there!" + name + ", you are" + age)

say_hi("Mike", "40") #This parameter inside say_hi is getting passed into the definition "name"
say_hi("Steve", "50") 

def say_bye(name, age):
    print("Good bye!" + name + ", you are" + str(age))

say_bye("Alex", 20) #you can also pass a straight integer but will have to add str before printing the value

#returning
def cube(num):
   return num*num*num #use return when using a function and it will send back the call
   #print("code") isn't going to work
result = cube(4)
print(result)

#if statements
is_male = True #if changed to false, it won't print
is_tall = True #if both conditions are false, print else statement
if is_male or is_tall: #"and" checks if both condeitions are met
    print("You are a male")
elif is_male and not(is_tall): #else if "elif" and ! is not()
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are tall but not male")
else:  
    print("You're neither male nor tall")

#comparison
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3, 4, 5)) #these numbers correspond to num1, 2, and 3. The greatest number out of these 3 numbers are 5, so it prints 5
#you can also use "==" to see if two variables match
#can also compare strings and booleans


