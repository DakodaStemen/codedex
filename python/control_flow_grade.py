#!/usr/bin/env python3

def eval_grade(grade: int) -> str:
    """Maps numeric grade to high school year label."""
    if grade == 9:
        return "Freshman"
    elif grade == 10:
        return "Sophomore"  # fixed typo
    elif grade == 11:
        return "Junior"
    elif grade == 12:
        return "Senior"
    else:
        return "TBD"

def main():
    try:
        user_input = input("\nPlease enter your grade (9–12): ").strip()
        grade = int(user_input)

        if not (9 <= grade <= 12):
            print("Error: Grade must be between 9 and 12.")
            return

        print(eval_grade(grade))

    except ValueError:
        print("Error: Please enter a valid whole number (e.g., 9, 10, 11, or 12).")

if __name__ == "__main__":
    main()
