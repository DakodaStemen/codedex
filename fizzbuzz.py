#----- print 1 - 100
for i in range(1, 101):
    # n % 3 == 0 && n % 5 == 0? -> FizzBuzz, check first
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    # n % 3 == 0? -> Fizz
    elif i % 3 == 0:
        print("Fizz")

    # n % 5 == 0? -> Buzz
    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)
