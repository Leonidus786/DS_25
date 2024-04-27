"""Ask the user to enter the number of day
and then show the output as weekday. And if user enters
a number other than 1-7 then print a message as invalid day."""

no_day = int(input("Enter the number between 1-7: "))

if no_day == 1:
    print("Monday")
elif no_day == 2:
    print("Tuesday")
elif no_day == 3:
    print("Wednesday")
elif no_day == 4:
    print("Thursday")
elif no_day == 5:
    print("Friday")
elif no_day == 6:
    print("Saturday")
elif no_day == 7:
    print("Sunday")
else:
    print("Invalid Day")