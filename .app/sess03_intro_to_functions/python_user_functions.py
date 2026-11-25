# This script/file demonstrates defining and calling/invoking user defined
# functions in Python

# Define a function to display a greeting message when called/invoked
def greeting(): # Does not take any parameters
   print("Hello from 'greeting()' function") # Doesn't return any value as well

# Call the 'greeting()' function
greeting()

# Define a function that accepts a parameter (user's name) and greets the user
def greet_user(username : str) -> None:
    print(f"Hello, {username} from Python functions!")

# Prompt the user for their name
name = input("Please enter your name:\n")

# Call the 'greet_user()' function and pass the user's name as a parameter
greet_user(name)

# Define a function that accepts two numbers and an operator ('+': default or 'x')
# to add or multiply them respectively
def add_or_multiply(first_num: int, second_num: int, operator:str = "+") -> int:
   """
   Adds or multiplies two numbers depending on specified operator. Defaults to '+' addition.

   Args:
      first_num (int): The first number to be used in the calculation.
      second_num (int): The second number to be used in the calculation.
      operator (str): The operator to be used in the calculation. Defaults to '+'.

   Returns:
      int: The sum or product of the two numbers.

   Examples:
      >>> add_or_multiply(2,3,'+')
      5
      >>> add_or_multiply(2,3,'*')
      6
      >>> add_or_multiply(2,5)
      7
      >>> add_or_multiply(4,3,'x')
      12
      >>> add_or_multiply(4,3,'-')
      Invalid operation!
      Please use "+" or "x"
   """
   if operator == "+":
      return first_num + second_num
   elif operator == "*" or operator == "x":
      return first_num * second_num
   else:
      print("Invalid operator!\nPlease use '+' or 'x'.")
      return

# Invoke/call the 'add_or_multiply()' function
print(f"The sum of 3 and 5 is {add_or_multiply(3,5)}")
print("The product of %d and %d is %d." % (3, 5, add_or_multiply(3,5,operator="x")))

# Display the documentation string of the 'add_or_multiply()' function
print(f"The documentation string of the 'add_or_multiply()' function is:\n"
      f" {add_or_multiply.__doc__}")

# Anonymous function(s)
# An anonymous/lamda function is a way to write a small compact function quickly. They are often
# used when you need a simple function for a short period and don't want to write a full function
# using the 'def' keyword
plus_five = lambda num: num + 5 # use a lambda to add 5 to a number
print(f"The sum of 7 and 5 using a lambda(anonymous function) is: {plus_five(7)}")

# The same functionality above using a normal function
def add_five(num):
   return num + 5  # Define a function to add 5 to the number/value passed in

# Call/invoke the add_five() function
print(f"The sum of 2 and 5 using a normal function is: {add_five(2)}")

# Anonymous/lambda function to get the difference between 2 numbers
difference = lambda num1, num2: num1 - num2

# Sample usage of the 'difference' lambda
print(f"The difference of 3 and 5 is: {difference(3,5)}")

# Function with variable parameters
# Define a function that accepts a varying number of parameters
def get_sum(*values):
   # sum = 0
   # for value in values:
   #    sum += value
   # return sum
   """
   Return the sum of all numeric values provided.

   Args:
       *values: A variable number of numeric values to sum.

   Returns:
       int or float: The sum of the provided values.

   Raises:
       TypeError: If any of the provided values is not numeric.

   Examples:
       >>> get_sum(1, 2, 3)
       6
       >>> get_sum(3.5, 2.1, 1.4)
       7.0
       >>> get_sum(1, 2, "3")
       TypeError: All values provided must be numbers/numeric values.
   """
   try:
      return sum(values) # succinct code, does the same thing as the four lines above
   except TypeError as te:
      raise TypeError("All values provided must be numbers/numeric values!") from te

# Create lists of numbers
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums_with_decimals = [4.5, 1.5, 2.0]
mixed_nums = [4.5, 1.5,'7']

# Code that may raise exceptions
try:
   print(f"The sum of the first ten integers is: {get_sum(*num_list)}")
   print(f"The sum of 4.5, 1.5, and 2.0 is: {get_sum(*nums_with_decimals)}")
   print(f"The sum of 4.5, 1.5, and '7' is: {get_sum(*mixed_nums)}")
except TypeError as te:
   print(f"{te}")







# predict the output of emails[1::2], fruits[-3:] and nums[::-2]