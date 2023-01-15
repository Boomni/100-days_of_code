
age = input("What is your current age? ")

years = 90 - int(age)
days = 365 * years
weeks = 52 * years
months = 12 * years

message = "You have {} days, {} weeks, and {} months left."

print(message.format(days, weeks, months))
