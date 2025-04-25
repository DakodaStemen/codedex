# Write code below 💖

try:
    month = int(input("Which month is it? [1 - 12]"))


    if month == 1 or month == 2 or month == 3:
        print('Winter 🌨️')
    elif month == 4 or month == 5 or month == 6:
        print('Spring 🌱')
    elif month == 7 or month == 8 or month == 9:
        print('Summer 🌻')
    elif month == 10 or month == 11 or month == 12:
        print('Autumn 🍂')
    else:
        print('Please enter a valid month number [1-12].')
except ValueError:
    print('Please enter a valid number.')