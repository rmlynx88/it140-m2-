import datetime

# Ask the user for their name and age
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

# Calculate the approximate birth year
current_year = datetime.datetime.now().year
birth_year = current_year - age

# Display the final greeting and calculated birth year
print(f"Hello {name}! You were born in {birth_year}.")
