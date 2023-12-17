# looping.py

def happy_new_year():
    count = 10
    while count > 0:
        print(count)
        count -= 1
    print("Happy New Year!")

def square_integers(numbers):
    return [num ** 2 for num in numbers]

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
