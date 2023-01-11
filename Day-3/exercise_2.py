"""
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Example Input
weight = 85
height = 1.75
Example Output
85 ÷ (1.75 x 1.75) = 27.755102040816325

Your BMI is 28, you are slightly overweight.
"""
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / (height ** 2))
if bmi < 18.5:
    print("Your BMI is {}, you are underweight.".format(bmi))
elif 18.5 < bmi < 25:
    print("Your BMI is {}, you have a normal weight.".format(bmi))
elif 25 < bmi < 30:
    print("Your BMI is {}, you are slightly overweight.".format(bmi))
elif 30 < bmi < 50:
    print("Your BMI is {}, you are obese.".format(bmi))
else:
    print("Your BMI is {}, you are clinically obese.".format(bmi))
