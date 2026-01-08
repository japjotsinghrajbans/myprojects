"""
author: Japjot Singh Rajbans
date: 1 March 2025
title: Multi-purpose Calculator
"""

import time
import math # I need the math function for square root

# Start menu
menu = input(">>> Welcome! What can I help with?\n>>> 1) Addition\n>>> 2) Subtraction\n>>> 3) Multiplication\n>>> 4) Division\n>>> 5) Exponentiation\n>>> 6) Square Root\n>>> 7) Percentage\n>>> 8) Credits\n> ").lower()

# Addition
if menu == "addition" or menu == "1":
    number_addition = int(input(">>> Alright, how many numbers would you like to add?\n> "))
    total_sum = 0
    for i in range(number_addition):
        number = int(input(f">>> Alright! Now please enter number {i + 1}: "))
        total_sum += number
    print(f">>> Alright, so your final answer is {total_sum}! :)")

# Subtraction
elif menu == "subtraction" or menu == "2":
    number_subtraction = int(input(">>> Alright, how many numbers would you like to subtract?\n> "))
    total_difference = 0
    for i in range(number_subtraction):
        if i == 0:
            total_difference = int(input(f">>> Alright! Now please enter number {i + 1}: "))
        else:
            number = int(input(f">>> Now, enter the number to subtract (number {i + 1}): "))
            total_difference -= number
    print(f">>> Alright, so your final answer is {total_difference}! :)")

# Multiplication
elif menu == "multiplication" or menu == "3":
    number_multiplication = int(input(">>> Alright, how many numbers would you like to multiply?\n> "))
    total_product = 1
    for i in range(number_multiplication):
        number = int(input(f">>> Alright! Now please enter number {i + 1}: "))
        total_product *= number
    print(f">>> Alright, so your final answer is {total_product}! :)")

# Division
elif menu == "division" or menu == "4":
    number_division = int(input(">>> Alright, how many numbers would you like to divide?\n> "))
    total_quotient = 0
    for i in range(number_division):
        if i == 0:
            total_quotient = int(input(f">>> Alright! Now please enter number {i + 1}: "))
        else:
            number = int(input(f">>> Now, enter the number to divide by (number {i + 1}): "))
            if number == 0:
                print(">>> Uh oh! Division by zero is not allowed! The program will now shut down.")
                exit()
            total_quotient /= number
    print(f">>> Alright, so your final answer is {total_quotient}! :)")

# Exponentiation (Exponents/Power)
elif menu == "exponentiation" or menu == "5":
    base = int(input(">>> Alright! Now enter the base number: "))
    exponent = int(input(">>> Hmm! Now the exponent number: "))
    result = base ** exponent
    print(f">>> Whew! So the result of {base} raised to the power of {exponent} is {result}! :)")

# Square Root
elif menu == "square root" or menu == "6":
    number = int(input(">>> Alright! Now enter the number to find the square root of: "))
    if number < 0:
        print(">>> The square root of a negative number is not real! Please enter a non-negative number.")
    else:
        print(f">>> *finding the root of {number}*")
        time.sleep(1)
        result = math.sqrt(number)
        print(f">>> Whew! Finally, the square root of {number} is {result}! :)")

# Percentage Calculation
elif menu == "percentage" or menu == "7":
    part = float(input(">>> Okay! Now enter the part value: "))
    time.sleep(1)
    whole = float(input(">>> Alright! Now enter the whole value: "))
    time.sleep(1.5)
    if whole == 0:
        print(">>> Hey! The whole value cannot be zero! Please enter a proper number.")
    else:
        percentage = (part / whole) * 100
        print(f">>> Hmm! In the end, the percentage of {part} out of {whole} is {percentage}%! :)")

# Credits
elif menu == "8" or menu == "credits":
    time.sleep(1)
    print(">>> *recalling credits*")
    time.sleep(0.5)
    print(">>> *typing*")
    time.sleep(1)
    print(">>> The owner and developer of this program is Japjot Singh Rajbans.")
    time.sleep(3)
    print(">>> *typing*")
    time.sleep(0.75)
    print(">>> This program, or rather, calculator, was made on 1 March 2025.")
    time.sleep(2.4)
    print(">>> *typing a long phrase*")
    time.sleep(2)
    print(">>> It took Japjot more than 3 days to make this program! And I would appreciate if you could give feedback on this program. Your feedback can be anything, from improvements to recommendations! You name it.")
    time.sleep(4.5)
    print(">>> *typing*")
    time.sleep(1.25)
    print(">>> Thank you for using this experimental calculator app, and have a great day! :)")

# If the person enters something else or types random stuff
else:
    print(">>> Uh oh! It looks like you typed something else. Restart the program and try again!")