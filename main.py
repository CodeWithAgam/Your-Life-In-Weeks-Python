# If you were to live 90 years,the below function calculates the 
# no. of days, weeks and months remaining in your life
# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @agamdeep_21, @coderagam001
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

# Print a welcome message
print("Welcome to Your Life In Weeks!")
print("what if you were to live 90 years?")
print("Know excatly how much time you have left in your life!")

# Get the age of the user as an integer
age = int(input("\nEnter your current age: "))

# Get the total no. of days, weeks and months in a person's life
months_total = 90 * 12
weeks_total = 90 * 52
days_total = 90 * 365

# Get the values according to the current age
months_current = age * 12
weeks_current = age * 52
days_current = age * 365

# Get the remaining days, weeks and months
months_left = months_total - months_current
weeks_left = weeks_total - weeks_current
days_left = days_total - days_current

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")