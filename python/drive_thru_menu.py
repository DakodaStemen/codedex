combos = [
  'Cheeseburger',
  'Fries',
  'Soda',
  'Ice Cream',
  'Cookie'
]

def welcome():
    print("""Welcome to Phatazz Burgerz!
    
    Below is our super Menu... 
    +------------------+
    | 1 - Cheeseburger |
    | 2 - Fries        |
    | 3 - Soda         |
    | 4 - Ice Cream    |
    | 5 - Cookie       |
    +------------------+
    """)

# When taking in an item we must subtract 1 to reach the proper index via our list
def get_item(combos):
    choice = int(input("Which combo number would you like? "))

    if 1 <= choice <= 5:
        og_choice = choice
        choice -= 1     # This is what I was yappin' about earlier 
        print(f"\nYou have selected combo number {og_choice}! \n...Go ahead and run me thy money.")
    else:
        print("That is not an option...")

welcome()
get_item(combos)