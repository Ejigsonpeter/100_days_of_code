#greetings

print("welcome to the tip calculator")
print("What was the total bill ? \n")
bill = input()
print("What percentage tip would you like to give  ? 10, 12, or 15 ? ")
percent = input()
count = print("How many people to split the  bill ? ")
count = input()

total = float(bill) + (float(bill) * (int(percent)/100))
split = round((total/ int(count)),2)
print(f"each person should pay : ${split}")
