"""
Python tuples
A tuple is a built-in data type that represents an ordered collection of elements of the same type.
Tuples allow duplicates and are immutable (their elements cannot be modified).
Tuples are created using () rounded brackets/parentheses or the tuple() function.
Tuples are generally faster than lists as Python doesn't have to worry about growing or shrinking tuples.
Some tuple operations are given below:
"""
import numbers

# Create a tuple of fruits
fruits = ("blueberry",'orange','apple','banana',"avocado",'guava','blueberry')

# Display the length i.e. number of fruits in the fruits tuple
print(f"The number of elements/items (fruits) in the 'fruits' tuple is {len(fruits)}")

# Display the contents of a tuple (names of the fruits)
print(f"The fruits in the 'fruits' tuple are:\n{fruits}")

# Get and display the index of an element/item in the tuple
print(f"The index of 'avocado' is {fruits.index('avocado')}")

# Count and display the occurrences of 'blueberry' in the fruits tuple
print(f"Blueberry appears {fruits.count('blueberry')} times in the fruits tuple.")

# Combine two tuples to create a third one and display its contents
combined_fruits = fruits + ('kiwi',"watermelon", 'pineapple','dragon fruit')
print(f"The combined fruits tuple is:\n{combined_fruits}")

# Create a tuple that repeats the fruit tuple twice
fruits_repeated = fruits * 2
print(f"The 'fruits_repeated' tuple contains:\n{fruits_repeated}")

# Create a sorted tuple of fruits
sorted_fruits = sorted(fruits)
print(f"The 'fruits_sorted' tuple contains:\n{sorted_fruits}")

# Display the minimum and maximum items in the fruits tuple (least & highest fruit letterwise)
print(f"The least fruit letterwise is: {min(fruits)}"
      f"The highest fruit letterwise is: {max(fruits)}")

# Declare a tuple of numbers
numbers = (1,2,3,4,5);

# Display the tuple of numbers and its sum
print(f"The 'numbers' tuple contains:\n{numbers}, and their sum is: {sum(numbers)}")

# TODO: Add more tuple operations after learning about slicing in Python.
