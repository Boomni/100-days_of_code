# Day 4 - Randomisation and Python Lists

---
## Concepts Worked on
- Random Module
- Understanding the Offset and Appending Items to Lists
- Index Errors and Working with Nested Lists
- Rock Paper Scissors Game

---
## Exercises
<details><summary>Exercise 1</summary><br>

## Heads or Tails

### Instructions

You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails". 

**Important**, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.

e.g.
1 means Heads
0 means Tails 

#### Example Output

```
Heads
```

or

```
Tails
```
Solution: [Exercise 1](https://github.com/boomni/100-days_of_code/Day-4/exercise-1.py)
</details>

<details><summary>Exercise 2</summary><br>

## Who's Paying

### Instructions

You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill. 

**Important**: You are not allowed to use the `choice()` function.

**Line 8** splits the string `names_string` into individual names and puts them inside a **List** called `names`. For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name

#### Example Input

```
Angela, Ben, Jenny, Michael, Chloe
```
Note: notice that there is a space between the comma and the next name. 
#### Example Output

```
Michael is going to buy the meal today!
```
Solution: [Exercise 2](https://github.com/boomni/100-days_of_code/Day-4/exercise-2.py)
</details>

<details><summary>Exercise 3</summary><br>

## Treasure Map

## Instructions

You are going to write a program which will mark a spot with an X.

In the starting code, you will find a variable called ```map```.

This ```map``` contains a nested list.
When ```map``` is printed this is what the nested list looks like:
```
['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
```
In the starting code, we have used new lines (```\n```) to format the three rows into a square, like this:
```
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
```
This is to try and simulate the coordinates on a real map. 

![](https://res.cloudinary.com/dk-find-out/image/upload/q_80,w_1440,f_auto/Co-ordinates_oggjzg.jpg)

Your job is to write a program that allows you to mark a square on the map using a two-digit system. The first digit for the input will specify the column (the position on the horizontal axis). The second digit in the input will specify the row number (the position on the vertical axis). 

First your program must take the user input and convert it to a usable format. 

Next, you need to use it to update your nested list with an "x". 

#### Example Input 1

column 2, row 3 would be entered as:

```
23
```

#### Example Output 1

```
['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', 'X', '⬜️']
```

#### Example Input 2

column 3, row 1 would be entered as:

```
31
```

#### Example Output 2

```
['⬜️', '⬜️', 'X']

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']
```

![](https://cdn.fs.teachablecdn.com/5hliFjyIR96LdestyfPd)

Solution: [Exercise 3](https://github.com/boomni/100-days_of_code/Day-4/exercise-3.py)
</details>

---
## Project
### Rock Paper Scissors

<details><summary>Project Instruction</summary><br>

## Instructions

Make a rock, paper, scissors game. 

Inside the `main.py` file, you'll find the ASCII art for the hand signals already saved to a corresponding variable: `rock`, `paper`, and `scissors`. This will make it easy to print them out to the console. 

Start the game by asking the player:

*"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."*

From there you will need to figure out: 
* How you will store the user's input.
* How you will generate a random choice for the computer.
* How you will compare the user's and the computer's choice to determine the winner (or a draw).
* And also how you will give feedback to the player. 

You can find the "official" rules of the game on [the World Rock Paper Scissors Association website.](https://wrpsa.com/the-official-rules-of-rock-paper-scissors/

<details>
**Project Illustration**
![Rock Paper Scissors Illustration](https://github.com/Boomni/100-days_of_code/blob/main/images/rock_paper_scissors.gif)

---
