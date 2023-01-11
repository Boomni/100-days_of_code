print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name = name1 + name2
name = name.lower()
t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")
true = t + r + u + e
l = name.count("l")
o = name.count("o")
v = name.count("v")
love = l + o + v + e
score = int(true + love)
if (score < 10) or (score > 90):
  print("Your score is {}, you go together like coke and mentos.".format(score))
elif (loveInt <= 50) and (loveInt >= 40):
  print("Your score is {}, you are alright together.".format(score))
else:
  print("Your score is {}".format(score))
