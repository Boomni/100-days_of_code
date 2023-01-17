def prime_checker(number = 0):
    numbers = []
    for i in range(1, number + 1):
        numbers.append(i)
   
    divisors = []
    for i in numbers:
        if number % i == 0:
            divisors.append(i)

    if len(divisors) == 2:
        print("It's a Prime Number")
    else:
        print("It's Not a Prime Number")

n = int(input("Check this number: "))
prime_checker(number=n)
