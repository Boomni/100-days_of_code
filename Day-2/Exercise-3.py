"" "
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:
You have x days, y weeks, and z months left.
Where x, y and z are replaced with the actual calculated numbers.

Example Input
56
Example Output
You have 12410 days, 1768 weeks, and 408 months left.
"" "

# # 🚨 Don't change the code below 👇
# age = input("What is your current age? ")
# # 🚨 Don't change the code above 👆

#Write your code below this line 👇
years = 90 - int(age)
days = 365 * years
weeks = 52 * years
months = 12 * years
message = "You have {} days, {} weeks, and {} months left."
printf(message.format(days, weeks, months))
