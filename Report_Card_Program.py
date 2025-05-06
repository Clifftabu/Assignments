# Simple: This is an integer number
# Dev: Declares a variable 'number' of type int
number = 10

# Simple: A decimal number (float)
# Dev: Declares a variable 'decimal' with float value
decimal = 2.5

# Simple: This is a True/False value
# Dev: Boolean variable 'active' is set to True
active = True

# Simple: A list containing two names
# Dev: List of strings stored in variable 'names'
names = ["John", "Doe"]

# Simple: Show the list of names on the screen
# Dev: Prints the contents of the 'names' list
print(names)


# Simple: This function takes a name and prints some info
# Dev: Function 'greet' with type hint for parameter 'name' (string)
def greet(name: str):
    # Simple: Show the name typed
    # Dev: Prints the name argument passed to the function
    print(name)
    print("-----------")

    # Simple: Fixed age used for comparison
    # Dev: Local variable 'age' set to 50
    age = 50

    # Simple: If the age is below 20, say 'adult' (note: logic seems off)
    # Dev: Conditional checks for age ranges
    if age < 20:
        print('teen')
    elif age > 50:
        print("adult")
    else:
        print("underage")  # Simple: This will print for age 50

    # Simple: Function ends without giving back a result
    # Dev: Explicitly returns None
    return None


# Simple: Count from 0 to 9 and show each number
# Dev: For-loop from 0 to 9 using range()
for i in range(10):
    print(i)

# Simple: Go through each character in the name and show it
# Dev: Loops through each character in the string "John Doe"
for i in "John Doe":
    print(i)

# Simple: If you're running this file directly (not importing), run the greet function
# Dev: Python entry-point check using __name__ == "__main__"
if __name__ == "__main__":
    greet("John")


# --- Part 2 of code below --- #

# Simple: Import 'Final' so we can create constants
# Dev: Final is used to define constant variables (from typing module)
from typing import Final


# Simple: Calculates area of a circle using radius
# Dev: Function that returns the area of a circle given a float radius
def area_circle(radius: float):
    # pi =3.14  # (commented out version)
    pi: Final = 3.14  # Constant value of π

    return pi * (radius ** 2)  # Simple: radius squared × pi


# Simple: Checks if average score is 50 or more
# Dev: Returns True if average is >= 50, else False
def has_passed(average: float) -> bool:
    return average >= 50


# Simple: Adds all scores and divides by how many there are to get average
# Dev: Computes the average of a list of integers
def compute_average(scores: list[int]) -> float:
    return sum(scores) / len(scores)


# Simple: This function handles the full student evaluation process
# Dev: Handles input, processing, and output of a student’s performance data
def students_performance() -> None:
    # Simple: Ask for the student's name
    name: str = input("Enter student name: ")

    # Simple: Show a greeting
    print(greet(name))

    scores: list[int] = []  # Simple: Empty list to hold subject scores

    # Simple: Loop 5 times to get 5 subject scores
    # Dev: Outer loop runs 5 times for 5 subjects
    for i in range(5):
        while True:  # Dev: Loop until valid input is given
            try:
                # Simple: Ask for a subject score
                score = int(input(f"Enter score  for subject{i + 1}: "))
                # Simple: Make sure the score is between 0 and 100
                if 0 <= score <= 100:
                    scores.append(score)
                    break  # Valid score, break out of loop
                else:
                    print("Please enter a score between 0 and 100: ")
            except ValueError:
                # Simple: This message appears if user types something that's not a number
                print("Please enter a valid number: ")

        # --- The following runs after all scores are collected --- #

        average_score: float = compute_average(scores)  # Simple: Calculate average
        is_pass: bool = has_passed(average_score)       # Simple: Check if student passed

        assignments_done: int = 5      # Simple: Fixed number of assignments
        pts: float = 2.5               # Simple: Extra points from assignments
        total_score: float = average_score + pts  # Simple: Final score with bonuses

        # Simple: Display the full report card
        print("\n---- Report Card ----")
        print(f"Name           : {name}")
        print(f"Scores         : {scores}")
        print(f"Average        : {average_score:.2f}")
        print(f"Status         : {'Pass' if is_pass else 'Fail'}")
        print(f"Assignments    : {assignments_done}")
        print(f"Extra Points   : {pts}")
        print(f"Final Score    : {total_score:.2f}")


# Simple: Call the function to start the student report process
# Dev: Execution of students_performance() if this script is run directly
students_performance()

# Simple: Just a note or variable versioning left at the bottom (not used)
# Dev: A constant version number (commented out)
# VERSION_NUMBER: Final ="1.2.9"
