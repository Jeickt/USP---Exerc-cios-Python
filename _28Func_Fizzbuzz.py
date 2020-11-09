def fizzbuzz(x):
    if x % 15 == 0:
        return "FizzBuzz"
    else:
        if x % 5 == 0:
            return "Buzz"
        elif x % 3 == 0:
            return "Fizz"
        else:
            return x