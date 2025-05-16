# Asking for the first number
first_number = float(input("Enter the first number:\n"))

# Asking for the second one
second_number = float(input("Enter the second number:\n"))

# The math itself:D
add = first_number + second_number
multi = first_number * second_number

# We need to check that the second number is not zero because it is impossible to divide by zero
if second_number == 0:
    div = "it is impossible to divide by zero"
else:
    div = first_number / second_number

# Results printing
print(f"Result of addition: {add}")
print(f"Result of multiplication: {multi}")
print(f"Result of division: {div}")