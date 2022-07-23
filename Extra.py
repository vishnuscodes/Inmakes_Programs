day_dictionary = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May",
                  6: "June", 7: "July", 8: "August", 9: "September", 10: "October",
                  11: "November", 12: "December"}

x = int(input("Enter the number : "))

if x <= 12:
    print(day_dictionary[x])

else:
    print("Invalid Number")
