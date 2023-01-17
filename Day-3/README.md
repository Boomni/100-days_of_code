# Day 3 - Control Flow and Logical Operators

---
## Concepts Worked on
- Control Flow with if / else and Conditional Operators
- Modulo Operator
- Nested if statements and elif statements
- Multiple If Statements in Succession
- Logical Operators
- Treasure Island game

---
## Exercises
<details><summary>Exercise 1</summary><br>

## Odd or Even

### Instructions

Write a program that works out whether if a given number is an odd or even number. 

Even numbers can be divided by 2 with no remainder. 

e.g. 86 is **even** because 86 ÷ 2 = 43

43 does not have any decimal places. Therefore the division is clean.

e.g. 59 is **odd** because 59 ÷ 2 = 29.5

29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.

The **modulo** is written as a percentage sign (%) in Python. It gives you the remainder after a division. 

e.g. 

6 ÷ 2 = 3 with no remainder. 

```
6 % 2 = 0
```

5 ÷ 2 = 2 x **2** + 1, remainder is 1.

```
5 % 2 = 1
```

14 ÷ 4 = 3 x **4** + 2, remainder is 2.

```
14 % 4 = 2
```

#### Example Input 1

```
43
```

#### Example Output 1

```
This is an odd number.
```

#### Example Input 2

```
94
```

#### Example Output 2

```
This is an even number.
```

Solution: [Exercise 1](https://github.com/Boomni/100-days_of_code/blob/main/Day-3/exercise_1.py)
</details>
<details><summary>Exercise 2</summary><br>

## BMI Calculator 2.0

### Instructions

Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

- Under 18.5 they are underweight
- Over 18.5 but below 25 they have a normal weight
- Over 25 but below 30 they are slightly overweight
- Over 30 but below 35 they are obese
- Above 35 they are clinically obese.

![](https://cdn.fs.teachablecdn.com/qTOp8afxSkGfU5YGYf36)

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

![](https://cdn.fs.teachablecdn.com/jKHjnLrNQjqzdz3MTMyv)

**Warning** you should **round** the result to the nearest whole number. The interpretation message needs to include the words in bold from the interpretations above. e.g. **underweight, normal weight,  overweight, obese, clinically obese**. 

#### Example Input

```
weight = 85
```

```
height = 1.75
```

#### Example Output

85 ÷ (1.75 x 1.75) =  27.755102040816325

```
Your BMI is 28, you are slightly overweight.
```

e.g. When you hit **run**, this is what should happen:   

![](https://cdn.fs.teachablecdn.com/mGRynIETXuVqoDk8unci)

The testing code will check for print output that is formatted like one of the lines below:

```
"Your BMI is 18, you are underweight."
"Your BMI is 22, you have a normal weight."
"Your BMI is 28, you are slightly overweight."
"Your BMI is 33, you are obese."
"Your BMI is 40, you are clinically obese."
```

Solution: [Exercise 2](https://github.com/Boomni/100-days_of_code/blob/main/Day-3/exercise_2.py)
</details>
<details><summary>Exercise 3</summary><br>

## Leap Year

### Instructions

Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:

[https://www.youtube.com/watch?v=xX96xng7sAE](https://www.youtube.com/watch?v=xX96xng7sAE)

This is how you work out whether if a particular year is a leap year. 

> `on every year that is evenly divisible by 4
>   **except** every year that is evenly divisible by 100
>     **unless** the year is also evenly divisible by 400`

e.g. The year 2000:

2000 ÷ 4 = 500 (Leap)

2000 ÷ 100 = 20 (Not Leap)

2000 ÷ 400 = 5 (Leap!)

So the year 2000 is a leap year.

But the year 2100 is not a leap year because:

2100 ÷  4 = 525 (Leap)

2100 ÷ 100 = 21 (Not Leap)

2100 ÷ 400 = 5.25 (Not Leap)

**Warning** your output should match the Example Output format exactly, even the positions of the commas and full stops. 

#### Example Input 1

```
2400
```

#### Example Output 1

```
Leap year.
```

#### Example Input 2

```
1989
```

#### Example Output 2

```
Not leap year.
```

 ![](https://cdn.fs.teachablecdn.com/AthNqKoSm6JD4sMom2X2)

Solution: [Exercise 3](https://github.com/Boomni/100-days_of_code/blob/main/Day-3/exercise_3.py)
</details>

<details><summary>Exercise 4</summary><br>

## Pizza Order

### Instructions

Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program. 

Based on a user's order, work out their final bill. 

```
Small Pizza: $15
```

```
Medium Pizza: $20
```

```
Large Pizza: $25
```

```
Pepperoni for Small Pizza: +$2
```

```
Pepperoni for Medium or Large Pizza: +$3
```

```
Extra cheese for any size pizza: + $1
```

#### Example Input

```
size = "L"
```

```
add_pepperoni = "Y"
```

```
extra_cheese = "N"
```

#### Example Output

```
Your final bill is: $28.
```

![](https://cdn.fs.teachablecdn.com/p1evEkwQxGNR4WlolIb4)
  
Solution: [Exercise 4](https://github.com/Boomni/100-days_of_code/blob/main/Day-3/exercise_4.py)
</details>
<details><summary>Exercise 5</summary><br>

## Love Calculator

### Instructions

You are going to write a program that tests the compatibility between two people.  

To work out the love score between two people:

> Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number. 


For Love Scores **less than 10** or **greater than 90**, the message should be:

`"Your score is **x**, you go together like coke and mentos."` 

For Love Scores **between 40** and **50**, the message should be:

`"Your score is **y**, you are alright together."`

Otherwise, the message will just be their score. e.g.:

`"Your score is **z**."`

e.g. 

`name1 = "Angela Yu"`

`name2 = "Jack Bauer"`

T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."

#### Example Input 1

```
name1 = "Kanye West"
```

```
name2 = "Kim Kardashian"
```

#### Example Output 1

```
Your score is 42, you are alright together.
```

#### Example Input 2

```
name1 = "Brad Pitt"
```

```
name2 = "Jennifer Aniston"
```

#### Example Output 2

```
Your score is 73.
```

![](https://cdn.fs.teachablecdn.com/nfSILIPSNaIOwWhPR5vr)

The testing code will check for print output that is formatted like one of the lines below:
```
"Your score is 47, you are alright together."
"Your score is 125, you go together like coke and mentos."
"Your score is 54."
```

#### Score Comparison

Not sure you're getting the correct score for the exercise? Use this table to check your code's score against mine.

| Name 1 | Name 2 | Score |
| --- | --- | --- |
Catherine Zeta-Jones | Michael Douglas |99
Brad Pitt |	Jennifer Aniston	| 73
Prince William	| Kate Middleton	| 67
Angela Yu	| Jack Bauer	| 53
Kanye West	| Kim Kardashian	| 42
Beyonce	| Jay-Z	| 23
John Lennon	| Yoko Ono	| 18

Solution: [Exercise 5](https://github.com/Boomni/100-days_of_code/blob/main/Day-3/exercise_5.py)
</details>

---
## Project
### Treasure island
<details><summary>Project Instruction</summary><br>

## Instructions

Make your own "Choose Your Own Adventure" game. Use conditionals such as `if`, `else`, and `elif` statements to lay out the logic and the story's path in your program. 

[To write your code according to my story, you can use this flow chart from draw.io to help you.](https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload)

However, I think the fun part is writing your *own* story 😊

🧞‍♂️ 🐊 🧙‍♂️ 🧟 🧚‍♂️ 🧝‍♂️ 🥷 🤖 👽 🙀 

That said if you'd like to continue with my example, feel free to use the text snippets below...

### Text Snippets from my example

* 'You\'re at a crossroad. Where do you want to go? Type "left" or "right"'
* 'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.'
* "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?"
* "It\'s a room full of fire. Game Over."
* "You found the treasure! You Win!"
* "You enter a room of beasts. Game Over."
* "You chose a door that doesn\'t exist. Game Over."
* "You get attacked by an angry trout. Game Over."
* "You fell into a hole. Game Over."

#### Escaping Characters

If you want to use multiple sets of quotes inside a single string, you might have to "escape" some of them using the backslash `\`. You can see this in my first sentence: 'You\'re at a crossroad...'. [More on escaping characters here.](https://www.w3schools.com/python/gloss_python_escape_characters.asp)

#### Extensions

Have a think about how you might write your program to make a player's answers less case-sensitive. In other words, your code should work regardless of whether your user answers "left" or "Left".

[You can also add your own ASCII art](https://ascii.co.uk/art). Just remember to add three single quotes `'''` at the start and at the end of your artwork to turn it into a multi-line string. 

</details>

#### - Project Illustration

![Treasure island Illustration](https://github.com/Boomni/100-days_of_code/blob/main/images/treasure_island.gif)

---
