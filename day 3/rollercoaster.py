print("welcome to the rollercoaster program!!")
height = int(input("what is your height in cm ? "))
bill = 0
if height >= 120 :
    print("you can ride in the rollercoaster!!!")
    age = int(input("What is your Age:"))
    if age < 12:
        bill = 5
        print("please pay $5.")
    elif age <= 18:
        bill = 7
        print("please pay $7.")
    elif age >= 45 and age <= 55:
        print("Snap out of it bro")
    else:
        bill = 12
        print("please pay $12.")

    wants_photo = input("Do you want a phot taken ? Y or N ?" )
    if wants_photo == 'Y':
        bill += 3
    print (f"your bill id ${bill}")
   
else:
    print("Sorry, You have to grow taller to before you can ride ")