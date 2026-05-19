# Demonstrate how variables are created and how they work
# Author: Juergen Lier
# Date: 6 may 2026
# Version 1.1
# TODO:
#        Store a string
#        store different types of numbers
#        Assign the value of one variable to another
#        Do calcluations with variables and store the results

# Store a string
greeting = "Hello world" 
print (greeting)


# Store different types of numbers
# Storing an integer (whole number)
num_1 = 7
print(f"The variable called num_1 is a {type(num_1)}")

# Stores a float number ( a nr with a decimal)
num_2 = 9.5
print(f"The variable called num_2 is a {type(num_2)}")

# Assign the value of one variable to another
num_2 = greeting
print(f"num_2 has the value of{greeting}.")
print(f"num_2 has the value of{type(num_2)}.")


#  Do calcluations with variables and store the results

num_1 = 5

num_2 = 18

# add up numbers

sum = 5 + 18 # Not good practice
print(sum)
#prints as 23

sum = num_1 + num_2
print(sum)
# print as 23
# this is called concatenation
sum_string1 = "18"
sum_string2 = "5"

sum_string_total = sum_string1 + sum_string2
print(sum_string_total)
# Total prints as 185. This is not a number, it is text.

# print formatting.
# f stands for 'format'.
# Insert the value of the variable into the string
# using curly brackets.
print(f"my calculation for adding {num_1} and {num_2} together is {sum}")   
# old way of formatting
print("My calculation for concatenating {} and {} is {}".format(sum_string1,sum_string2,sum_string_total))

#greet someone
name = "Chrislou Geldenhuys"
print("Kia ora, my name is ",name)

print("Kia ora, my name is {}.".format(name))
print(f"Kia ora, my name is {name}.")
