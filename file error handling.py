# Creat an error handling function
# author : Louis WIllers
# Date: 08 May 2026
# Version 1

'''# Code that tests that a valid number is entered (V1)
done = False # Boolean variable steps to False
#while loop that runs until a valid number is entered
while not done:
    num = int(input("Please enter your number: "))
    done = True

print(f"The number you entered is {num}.")'''

# Version 2

# Code that tests that a valid number is entered (V2)
# Create a function to call everytime i ask the user
#for a number. A .
# I can use a function over and over. To use a function
# I 'call' it by writing out its name.
def test_int_num(): #0
    
    done = False
    while not done:
        try: # This tries for a valid input
            num = int(input("Please enter your number:  "))
            done = True

        except ValueError:
            print("that is not a valid integer.")

    return(num)


# Main routine
num_1 = test_int_num()
print(f"You entered {num_1} as your first number,")

num_2 = test_int_num()
print(f"You entered {num_2} as your second number.")

sum = num_1 + num_2
print(f"Your two numbers added together are {sum}")

multiply = num_1 * num_2
print(f"The number multiplied with each other results in {multiply}")

#division
divide = num_1 / num_2
print(f"{num_1} divided by {num_2} is equal to (divide).")

# Version 3. refining my code. Making it more pythonic.
#this will result in being able to change the question in the function
def test_int_num(question): # 'question' is a placeholder
    done = False
    while not done:
        print(question)
    try: # tries valid input
        num = int(input))
        if num >= low and num <=high:
            done = True

        else: print(error)
        print()
    
           

        except Value error:
            print("That is not a valid integer.")

# Main routine
num_1 = test_int_num("Please enter a number between 1 and 10:", 1, 10)
print(f"You entered {num_1}.\n")

num_2 = test_int_num("Please enter your second number :  ")
print(f"You entered {num_2}.\n")

num_3 = test_int_num("Please enter your third number :  ")
print(f"You entered {num_3}.\n")


num_1 = test_int_num()
print(f"You entered {num_1} as your first number,")

num_2 = test_int_num()
print(f"You entered {num_2} as your second number.")

sum = num_1 + num_2
print(f"Your two numbers added together are {sum}")

multiply = num_1 * num_2 * num_3
print(f"The number multiplied with each other results in {multiply}")

#division
divide = num_1 / num_2
print(f"{num_1} divided by {num_2} is equal to (divide).")

       
