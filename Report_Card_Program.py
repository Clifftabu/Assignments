number = 10
decimal = 2.5
active = True

names = ["John", "Doe"]

print(names)

def greet(name: str):
    print(name)
    print("-----------")
    age = 50
    if age < 20:
        print('teen')
    elif age > 50:
        print("adult")
    else:
        print("underage")
    return None

for i in "John Doe":
    print(i)

if __name__ == "__main__":
    greet("John")

# --- Part 2 of code below --- #
from typing import Final

def area_circle(radius: float):
    pi: Final = 3.14
    return pi * (radius ** 2)

def has_passed(average: float) -> bool:
    return average >= 50

def compute_average(scores: list[int]) -> float:
    return sum(scores) / len(scores)

def students_performance() -> None:
    name: str = input("Enter student name: ")
    print(greet(name))  # This will print None since greet() returns None

    scores: list[int] = []
    
    # Collect all 5 scores first
    for i in range(5):
        while True:
            try:
                score = int(input(f"Enter score for subject {i + 1}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Please enter a score between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    # FIXED: Moved report card generation outside the for loop
    average_score: float = compute_average(scores)
    is_pass: bool = has_passed(average_score)
    assignments_done: int = 5
    pts: float = 2.5
    total_score: float = average_score + pts

    print("\n---- Report Card ----")
    print(f"Name           : {name}")
    print(f"Scores         : {scores}")
    print(f"Average        : {average_score:.2f}")
    print(f"Status         : {'Pass' if is_pass else 'Fail'}")
    print(f"Assignments    : {assignments_done}")
    print(f"Extra Points   : {pts}")
    print(f"Final Score    : {total_score:.2f}")

students_performance()
