print("Welcome to the tip calculator.")
total = input("What was the total bill? $")
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")
tip = (float(total) / int(people)) * ((float(percentage) / 100) + 1)
print(round(tip, 2))