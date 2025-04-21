# Write code below 💖

def conversion():
    try:
        weight = float(input("What is your Earth weight?: "))
        planet = int(input("Which planet number would you like to convert?: "))

        if planet == 1:
            relative_gravity = weight * 0.38
        elif planet == 2:
            relative_gravity = weight * 0.91
        elif planet == 3:
            relative_gravity = weight * 0.38
        elif planet == 4:
            relative_gravity = weight * 2.53
        elif planet == 5:
            relative_gravity = weight * 1.07
        elif planet == 6:
            relative_gravity = weight * 0.89
        elif planet == 7: 
            relative_gravity = weight * 1.1
        else:
            print("Please enter a valid number from 1 - 7.")
            return  # Exit the function if the input is invalid

        print(f"Your weight on the selected planet is: {relative_gravity:.2f} kg")
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and planet.")

def main():
    conversion()

if __name__ == "__main__":
    main()