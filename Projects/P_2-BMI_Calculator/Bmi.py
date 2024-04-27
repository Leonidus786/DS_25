#Take the height and weight from the user.

height = float(input("enter your height in m:\n"))

weight = float(input("enter your weight in kg:\n"))


# for reference --> https://en.wikipedia.org/wiki/Body_mass_index

#Formula for calculating the BMI 

# bmi = round(weight / height ** 2)
# bmi = 18.4

# Int Range()
bmi = round(weight / height ** 2)

if bmi < 18.5:  # means bmi <= 18.4
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi< 30 :
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")