Assignments:

(Python assignments for ICS-2025 to practice recursion, object-oriented programming, and applying algorithms in clear, structured scripts.)
All files are organized in the main branch for easy cloning and local testing.

  Fib.py:
    - Defines three Fibonacci functions:
              1. Simple recursion.
              2. Recursion with manual dictionary caching.
              3. Recursion with @lru_cache for automatic caching.
          - Uses for loops to print Fibonacci sequences for different ranges.
          - Includes Tower of Hanoi function using recursion to print disk movements.
        concepts_practiced:
          - recursion
          - caching and optimization
          - using loops for testing


leap_year_program.py:
   - Defines a function to check if a given year is a leap year using if-else checks.
          - Uses input() to get year from user and prints whether it is a leap year.
        concepts_practiced:
          - conditionals
          - user input
          - function definition


Report_Card_Program.py:
   - Defines ShoppingCart class to:
              - Add items with name, quantity, and price.
              - Remove items by name.
              - Calculate total cost.
              - Display cart contents.
          - Defines DiscountedCart subclass to apply discounts by overriding calculate_total().
          - Defines TaxedCart subclass to apply tax by overriding calculate_total().
          - Uses a checkout(cart) function to display cart details and totals.
          - In main:
              - Creates instances of ShoppingCart, DiscountedCart, and TaxedCart.
              - Adds sample items and calls checkout() for each to display contents and totals.
        concepts_practiced:
          - object-oriented programming
          - inheritance and method overriding
          - polymorphism
          - working with lists and tuples


shoppingcart.py:
   - Defines ShoppingCart class to:
              - Add items with name, quantity, and price.
              - Remove items by name.
              - Calculate total cost.
              - Display cart contents.
          - Defines DiscountedCart subclass to apply discounts by overriding calculate_total().
          - Defines TaxedCart subclass to apply tax by overriding calculate_total().
          - Uses a checkout(cart) function to display cart details and totals.
          - In main:
              - Creates instances of ShoppingCart, DiscountedCart, and TaxedCart.
              - Adds sample items and calls checkout() for each to display contents and totals.
        concepts_practiced:
          - object-oriented programming
          - inheritance and method overriding
          - polymorphism
          - working with lists and tuples


zellerscongruence.py:
   - Defines DateCalculator class with:
              - Initialization storing year, month, and day.
              - get_day_of_week() using Zeller’s Congruence to calculate day of the week:
                  - Adjusts for January and February.
                  - Applies formula to calculate and map result to weekday names.
          - Creates an instance with a test date and prints the day of the week.
        concepts_practiced:
          - classes and encapsulation
          - applying mathematical formulas in code
          - using lists for mapping
          
          
          
HOW TO RUN:
    - clone: git clone https://github.com/clifftabu/assignments.git
    - navigate: cd assignments
    - run:
         python Fib.py
         python leap_year_program.py
         python Report_Card_Program.py
         python shoppingcart.py
         python zellerscongruence.py

  concepts_practiced_overall:
    - recursion
    - loops and input validation
    - conditionals
    - object-oriented programming (classes, inheritance, polymorphism)
    - applying real-world formulas
    - using caching for optimization
        
