# Python slicing operations
# Syntax: sequence[start:stop:step]
# start index is inclusive: Python includes the element at the starting index
# stop index is exclusive: Python excludes the element at the stopping index
# step determines the interval: A step of 2 selects every second element, while -1 reverses the sequence

# ============================================================
# 1. STRINGS
# ============================================================

str1 = "Hello"
str2 = "Python programming"

# Return the first character from a string
print(f"\n1. STRINGS")
print("-" * 50)

print(
    f"The first character in 'str1' is {str1[0]}, "
    f"in 'str2' is {str2[0]}"
)

# Characters starting from the 3rd one to the end,
# taking every third character
print(
    f"Characters starting from the 3rd one to the end "
    f"in 'str2' are: {str2[2::3]}"
)


# ============================================================
# 2. LISTS
# ============================================================

nums = [1, 2, 3, 4, 5, 6]

print(f"\n2. LISTS")
print("-" * 50)

# Values from index 1 to 3
print(
    f"Values from index 1 - 4 in the 'nums' list "
    f"are: {nums[1:4]}"
)

# Values from index 2 to one from last
print(
    f"Values from index 2 to one from last "
    f"in the 'nums' list are: {nums[2:-1]}"
)

# Values from last to first
print(
    f"Values from last to first in the 'nums' "
    f"list are: {nums[::-1]}"
)


# ============================================================
# 3. LISTS OF EMAIL ADDRESSES
# ============================================================

emails = [
    "john@gmail.com",
    "mary@yahoo.com",
    "peter@outlook.com",
    "jane@gmail.com",
    "david@hotmail.com",
    "susan@yahoo.com",
]

print(f"\n3. EMAIL ADDRESSES (LIST)")
print("-" * 50)

# Return the first three email addresses
print(f"First three emails: {emails[:3]}")

# Return emails from index 2 onwards
print(f"Emails from index 2 onwards: {emails[2:]}")

# Return every second email address
print(f"Every second email: {emails[::2]}")

# Return the email addresses in reverse order
print(f"Emails in reverse order: {emails[::-1]}")


# ============================================================
# 4. TUPLES OF FRUITS
# ============================================================

fruits = (
    "Apple",
    "Banana",
    "Orange",
    "Mango",
    "Pineapple",
    "Grapes",
    "Watermelon",
)

print(f"\n4. FRUITS (TUPLE)")
print("-" * 50)

# Return the first three fruits
print(f"First three fruits: {fruits[:3]}")

# Return fruits from index 2 to 5
print(f"Fruits from index 2 to 5: {fruits[2:5]}")

# Return every second fruit
print(f"Every second fruit: {fruits[::2]}")

# Return the fruits in reverse order
print(f"Fruits in reverse order: {fruits[::-1]}")


# ============================================================
# 5. SETS
# ============================================================

email_set = {
    "john@gmail.com",
    "mary@yahoo.com",
    "peter@outlook.com",
    "jane@gmail.com",
    "david@hotmail.com",
}

print(f"\n5. SETS")
print("-" * 50)

print(f"Email set: {email_set}")

# Sets do not support indexing or slicing.
# The following operation would raise a TypeError:
#
# print(email_set[0:3])

print(
    "Sets do not support slicing because "
    "they are unordered collections."
)

# If slicing is required, convert the set into a list.
email_list = list(email_set)

print(
    f"First three emails after converting "
    f"the set to a list: {email_list[:3]}"
)
