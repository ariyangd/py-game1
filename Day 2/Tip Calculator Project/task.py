# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10 12 15 "))
# people = int(input("How many people to split the bill? "))



print("Welcome to the tip calculator!")

bill = float(input("what was the bill"))
tip = int(input("What is the tip percentage"))
people = int(input("Split to how many people"))

tipPercentage = (bill*tip)/100
calculation = ((bill + tipPercentage)/people)
print(calculation)