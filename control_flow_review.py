#!/usr/bin/env python3

"""
Rating Evaluator
Accepts user rating input (0–5) and prints a qualitative label.
Handles invalid inputs gracefully.
"""

def evaluate_rating(rating: float) -> str:
    """Returns qualitative label based on numeric rating."""
    if rating > 4.5:
        return "Extraordinary"
    elif rating > 4:
        return "Excellent"
    elif rating > 3:
        return "Good"
    elif rating > 2:
        return "Fair"
    else:
        return "Poor"

def main():
    try:
        user_input = input("\nEnter your rating (0–5): ").strip()
        rating = float(user_input)

        if not 0 <= rating <= 5:
            print("Error: Rating must be between 0 and 5.")
            return

        print(evaluate_rating(rating))

    except ValueError:
        print("Error: Please enter a valid number between 0 and 5.")

if __name__ == "__main__":
    main()
