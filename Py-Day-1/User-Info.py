# Write a Python program that asks the user to input their information, then displays it:
# Full Name
# Age
# Faculty
# University
# Graduation year

f_name = input("What is your first name? ")
l_name = input("What is your last name? ")
full_name = f_name + " " + l_name
age = input("What is your age? ")
faculty = input("What is your faculty? ")
university = input("What is your university? ")
graduation_year = input("What is your graduation year? ")
print("\n")

print("Welcome, " + full_name + "!")
print("Your age is " + age)
print("You graduated from Faculity of " +
      faculty + ", " + university + " University")
print("Your graduation year is " + graduation_year)
