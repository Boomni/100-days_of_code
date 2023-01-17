print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

all_names = (name1 + name2).lower()
t = all_names.count("t")
r = all_names.count("r")
u = all_names.count("u")
e = all_names.count("e")
l = all_names.count("l")
o = all_names.count("o")
v = all_names.count("v")

true = t + r + u + e
love = l + o + v + e
true = int(str(true) + "0")

score = true + love

if (score < 10) or (score > 90):
    print("Your score is {}, you go together like coke and mentos.".format(
        score))
elif (score >= 40) and (score <= 50):
    print("Your score is {}, you are alright together.".format(score))
else:
    print("Your score is {}.".format(score))
