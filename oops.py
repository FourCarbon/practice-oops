# Variables and basic types/practice program
name = "Alice"          # String (str)
age = 25                # Integer (int)
height = 5.6            # Float (float)
is_student = True       # Boolean (bool)

# Conditional statements (adult or minor)
if age >= 18:
    print(f"{name} is an adult.")
else:
    print(f"{name} is a minor.")

# For loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While loop
count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1



def calculate_area(length, width):
    return length * width

# Calling the function
area = calculate_area(5, 3)
print(f"Area: {area}")
